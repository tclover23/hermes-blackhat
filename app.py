from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    return jsonify({'response': f"[{data.get('mode','cloud').upper()}] {data.get('msg','')}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
