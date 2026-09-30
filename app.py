from flask import Flask, jsonify
import os

app = Flask(__name__)
print("====================Lucky Jha ===================================")
@app.get("/")
def home():
    print("************Home Point************")
    return jsonify(
        message="Hello from lucky jha using flask",
        platform="Github Actions",
        runtime="Docker + Flask"
    )

@app.get("/health")
def health():
    print("************Health Point************")
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))