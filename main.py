# app.py (for Flask example)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Basic App to learn DevOps - Ayushi"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
