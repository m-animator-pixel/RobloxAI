import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server running"

@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    prompt = data.get("prompt","")

    return jsonify({
        "response": "AI says: " + prompt
    })
