from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)
genai.configure(api_key=os.getenv("AIzaSyCw0ZplxiBf5KFPPLdUA7G3EWzhc81FqMk"))

model = genai.GenerativeModel("gemini-pro")

@app.route('/gemini', methods=['POST'])
def gemini_reply():
    data = request.json
    user_input = data.get("text", "")

    response = model.generate_content(user_input)
    reply = response.text

    return jsonify({"output": reply})
