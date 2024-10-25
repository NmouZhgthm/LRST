from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return jsonify({
            "status": "success",
            "message": "LRST API is running",
            "timestamp": time.time(),
            "region": "US East (Washington DC)"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/ping')
def ping():
    return jsonify({"pong": time.time()})

# Vercel 需要这个
app = app.wsgi_app
