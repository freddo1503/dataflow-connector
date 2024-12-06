import os
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Get backend URL from environment variables
BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/button-click")
def button_click():
    try:
        response = requests.get(f"{BACKEND_URL}/button-click")
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"message": "Error from backend"}), response.status_code
    except Exception as e:
        return jsonify({"message": f"Error connecting to backend: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
