from flask import Flask, jsonify

main = Flask(__name__)

@main.route('/')
def index():
    return jsonify({"Status": "Online"})
