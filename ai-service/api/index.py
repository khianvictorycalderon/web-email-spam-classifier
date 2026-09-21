import os

import joblib

from flask import Flask, request


# -------------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "spam_classifier.joblib"
)

VECTORIZER_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "tfidf_vectorizer.joblib"
)


# -------------------------------------------------------------------------
# INITIATE APP
# -------------------------------------------------------------------------

app = Flask(__name__)


# -------------------------------------------------------------------------
# LOAD MODEL
# -------------------------------------------------------------------------

print("Loading spam classifier...")

model = joblib.load(MODEL_PATH)

print("Spam classifier loaded successfully!")


# -------------------------------------------------------------------------
# LOAD VECTORIZER
# -------------------------------------------------------------------------

print("Loading TF-IDF vectorizer...")

vectorizer = joblib.load(VECTORIZER_PATH)

print("TF-IDF vectorizer loaded successfully!")


# -------------------------------------------------------------------------
# HEALTH CHECK
# -------------------------------------------------------------------------

@app.route("/health")
def health():
    return {
        "status": "AI Service: Healthy"
    }, 200


# -------------------------------------------------------------------------
# PREDICTION
# -------------------------------------------------------------------------

@app.route("/api/classify", methods=["POST"])
def predict():

    data = request.get_json()

    email_content = data["emailContent"]

    # Convert the email text into TF-IDF features.
    email_vectorized = vectorizer.transform(
        [email_content]
    )

    # Get probabilities.
    probabilities = model.predict_proba(
        email_vectorized
    )

    # Probability of class 1 (spam).
    spam_probability = probabilities[0][1]

    return {
        "classification": float(spam_probability)
    }, 200