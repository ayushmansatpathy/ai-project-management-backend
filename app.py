from flask import Flask, request, jsonify
from index import return_json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/response", methods=["GET"])
def response(prompt):
    try:
        prompt = request.json["data"]
        result = return_json(prompt)  # Call the function from index.py
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
