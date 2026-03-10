from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "AI server running"

@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    prompt = data.get("message","")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role":"user","content":prompt}
        ]
    }

    r = requests.post(API_URL, headers=headers, json=payload)
    response = r.json()

    try:
        text = response["choices"][0]["message"]["content"]
    except:
        text = "AI error"

    return jsonify({"response": text})
