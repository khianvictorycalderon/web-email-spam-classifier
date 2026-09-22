import os

import tensorflow as tf

from flask import Flask, request


# -------------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "spam_classifier.keras"
)


# -------------------------------------------------------------------------
# INITIATE APP
# -------------------------------------------------------------------------

app = Flask(__name__)


# -------------------------------------------------------------------------
# LOAD MODEL
# -------------------------------------------------------------------------

print("Loading spam classifier...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Spam classifier loaded successfully!")


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

    email_content = data["email_content"]

    # The TextVectorization layer is built into the model, so it accepts
    # the raw email text directly - no separate vectorizer needed.
    input_tensor = tf.constant([[email_content]])

    probabilities = model.predict(input_tensor)

    # Probability of class 1 (spam).
    spam_probability = float(probabilities[0][0])

    return {
        "classification": spam_probability
    }, 200