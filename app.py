from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/test')
def test():
    return jsonify({
        "status": "success",
        "message": "LRST API is running",
        "timestamp": time.time()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
