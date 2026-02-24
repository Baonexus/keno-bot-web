
from flask import Flask
from bot import run_bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot đang chạy OK!"

@app.route("/run")
def run():
    run_bot()
    return "Bot đã chạy xong!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
