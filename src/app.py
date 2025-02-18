from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("transformer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    review = data.get("review", "")

    # Preprocess and transform input
    x = vectorizer.transform([review])
    prediction = model.predict(x)[0]

    # Response
    response = {"review": review, "sentiment": prediction}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
