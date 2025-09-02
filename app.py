from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify(message="Olá! Esta é uma API da matéria de DevOps. Estamos na fase 2!!")

@app.route('/status', methods=['GET'])
def status():
    return jsonify(status="UP", message="tudo funcionando!!!")

@app.route('/about', methods=['GET'])
def about():
    return jsonify(project="DevOps Fase 2", author="Gabi", version="1.0")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
