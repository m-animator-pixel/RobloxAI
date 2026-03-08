from flask import Flask, request, jsonify
import os

app = Flask(__name__)
history = {}

@app.route("/")
def home():
    return "AI server working"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    player_id = data.get("player_id", "default")
    prompt = data.get("prompt", "")

    convo = history.get(player_id, [])
    response = f"AI: I understood your message: '{prompt}'"
    convo.append((prompt, response))
    history[player_id] = convo[-10:]
    return jsonify({"text": response})

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)