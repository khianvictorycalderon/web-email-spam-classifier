from flask import Flask

# Initiate the app
app = Flask(__name__)

# Test
@app.route("/")
def home():
    return {
        "message": "AI service is working!"
    }, 200

@app.route("/predict", method=["POST"])
def predict():
    return {
        "prediction": 0.5, # Let's just pretend this is a real prediction for now.
        "message": "Predicted successfully!"
    }

# Your AI inferencing here...
# For training, create a separate train.py or something similar then save the model.