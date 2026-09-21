# train.py

import argparse
import os

import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# -------------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------------

TRAINING_DATA_PATH = "dataset/spam.csv"

MODEL_DIR = "models"

MODEL_SAVE_PATH = os.path.join(
    MODEL_DIR,
    "spam_classifier.joblib"
)

VECTORIZER_SAVE_PATH = os.path.join(
    MODEL_DIR,
    "tfidf_vectorizer.joblib"
)


# -------------------------------------------------------------------------
# COMMAND-LINE ARGUMENTS
# -------------------------------------------------------------------------

parser = argparse.ArgumentParser(
    description="Train the email spam classification model."
)

parser.add_argument(
    "--overwrite",
    action="store_true",
    help="Train a new model from scratch."
)

args = parser.parse_args()


# -------------------------------------------------------------------------
# PREPARE MODEL DIRECTORY
# -------------------------------------------------------------------------

os.makedirs(MODEL_DIR, exist_ok=True)


# -------------------------------------------------------------------------
# LOAD DATASET
# -------------------------------------------------------------------------

print("Loading dataset...")

data = pd.read_csv(TRAINING_DATA_PATH)

print(f"Loaded {len(data)} samples.")


# -------------------------------------------------------------------------
# EXTRACT FEATURES AND TARGET
# -------------------------------------------------------------------------

texts = data["text"]
labels = data["label"]


# Convert labels:
#
# spam -> 1
# ham  -> 0

labels = labels.map({
    "ham": 0,
    "spam": 1
})


# -------------------------------------------------------------------------
# TRAIN / TEST SPLIT
# -------------------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    texts,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)


# -------------------------------------------------------------------------
# TEXT VECTORIZATION
# -------------------------------------------------------------------------

print("Creating TF-IDF vectorizer...")

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=10000
)

X_train_vectorized = vectorizer.fit_transform(X_train)

X_test_vectorized = vectorizer.transform(X_test)


# -------------------------------------------------------------------------
# CREATE MODEL
# -------------------------------------------------------------------------

print("Creating classifier...")

model = LogisticRegression(
    max_iter=1000
)


# -------------------------------------------------------------------------
# TRAIN MODEL
# -------------------------------------------------------------------------

print("Training model...")

model.fit(
    X_train_vectorized,
    y_train
)


# -------------------------------------------------------------------------
# EVALUATE MODEL
# -------------------------------------------------------------------------

print("Evaluating model...")

predictions = model.predict(X_test_vectorized)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Accuracy: {accuracy:.4f}")

print("\nClassification report:")
print(
    classification_report(
        y_test,
        predictions
    )
)


# -------------------------------------------------------------------------
# SAVE MODEL
# -------------------------------------------------------------------------

print("Saving model...")

joblib.dump(
    model,
    MODEL_SAVE_PATH
)


# -------------------------------------------------------------------------
# SAVE VECTORIZER
# -------------------------------------------------------------------------

print("Saving TF-IDF vectorizer...")

joblib.dump(
    vectorizer,
    VECTORIZER_SAVE_PATH
)


print("\nTraining complete!")
print(f"Model saved to: {MODEL_SAVE_PATH}")
print(f"Vectorizer saved to: {VECTORIZER_SAVE_PATH}")