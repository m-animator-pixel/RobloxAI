import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Prosta historia rozmowy w pamięci (na razie do restartu kontenera)
conversation_history = []

@app.route("/")
def home():
    return "AI server running"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    if not data or "prompt" not in data:
        return jsonify({"error": "No prompt provided"}), 400

    prompt = data["prompt"]
    
    # Dodaj prompt do historii
    conversation_history.append({"user": prompt})
    
    # Tu wstaw prosty "AI response"
    response_text = f"AI odpowiada na: {prompt}"  # <-- tutaj możesz wstawić własną logikę AI
    
    # Dodaj odpowiedź do historii
    conversation_history.append({"ai": response_text})
    
    return jsonify({
        "prompt": prompt,
        "response": response_text,
        "history": conversation_history
    })

# Użyj portu z Railway
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
