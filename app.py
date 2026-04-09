from flask import Flask, request, jsonify
from model import load_all, predict_top_words

app = Flask(__name__)

model, tokenizer, max_len = load_all()

@app.route("/")
def home():
    return "🚀 AI API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Empty input"})

    words = predict_top_words(model, tokenizer, text, max_len)

    return jsonify({"next_words": words})


if __name__ == "__main__":
    app.run(debug=True)