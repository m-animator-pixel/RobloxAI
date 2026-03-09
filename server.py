from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    return jsonify({
        "response": "AI response: " + prompt
    })
