from flask import Flask, send_from_directory
from flask_cors import CORS
from app.routes import api
import os

app = Flask(__name__, static_folder="static")
CORS(app)

# Register API blueprint
app.register_blueprint(api)

# Serve static files
@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route("/")
def home():
    return "✅ BabyCare API is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
