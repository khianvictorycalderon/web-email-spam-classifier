# train.py

import argparse
import os

import pandas as pd
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# -------------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------------

TRAINING_DATA_PATH = "dataset/spam.csv"

MODEL_DIR = "models"

MODEL_SAVE_PATH = os.path.join(
    MODEL_DIR,
    "spam_classifier.keras"
)

MAX_TOKENS = 10000
SEQUENCE_LENGTH = 200
EMBEDDING_DIM = 64
EPOCHS = 15
BATCH_SIZE = 32


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

texts = data["text"].astype(str)
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

X_train = X_train.to_numpy()
X_test = X_test.to_numpy()
y_train = y_train.to_numpy()
y_test = y_test.to_numpy()


# -------------------------------------------------------------------------
# TEXT VECTORIZATION
# -------------------------------------------------------------------------

print("Creating TextVectorization layer...")

vectorize_layer = tf.keras.layers.TextVectorization(
    max_tokens=MAX_TOKENS,
    standardize="lower_and_strip_punctuation",
    output_mode="int",
    output_sequence_length=SEQUENCE_LENGTH
)

# Learn the vocabulary from the training texts only.
vectorize_layer.adapt(X_train)


# -------------------------------------------------------------------------
# BUILD MODEL
# -------------------------------------------------------------------------

print("Creating classifier...")

# The TextVectorization layer is baked directly into the model, so the
# saved model accepts raw strings as input (no separate vectorizer file
# needs to be loaded/managed downstream).

inputs = tf.keras.Input(shape=(1,), dtype=tf.string)

x = vectorize_layer(inputs)
x = tf.keras.layers.Embedding(
    input_dim=MAX_TOKENS,
    output_dim=EMBEDDING_DIM,
    mask_zero=True
)(x)
x = tf.keras.layers.GlobalAveragePooling1D()(x)
x = tf.keras.layers.Dense(32, activation="relu")(x)
x = tf.keras.layers.Dropout(0.3)(x)
outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)

model = tf.keras.Model(inputs, outputs)

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()


# -------------------------------------------------------------------------
# TRAIN MODEL
# -------------------------------------------------------------------------

print("Training model...")

early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)

model.fit(
    X_train,
    y_train,
    validation_split=0.1,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    callbacks=[early_stopping]
)


# -------------------------------------------------------------------------
# EVALUATE MODEL
# -------------------------------------------------------------------------

print("Evaluating model...")

probabilities = model.predict(X_test).ravel()
predictions = (probabilities >= 0.5).astype(int)

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

model.save(MODEL_SAVE_PATH)


print("\nTraining complete!")
print(f"Model saved to: {MODEL_SAVE_PATH}")