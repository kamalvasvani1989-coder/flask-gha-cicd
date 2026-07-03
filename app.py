"""Simple Flask web application used for the CI/CD pipeline assignment."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello from the Flask CI/CD demo app!")


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


def add(a, b):
    """Tiny helper so we have pure-Python logic to unit test."""
    return a + b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
