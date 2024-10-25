from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from LRST!"  # 先用简单的返回测试

@app.route('/api/test')
def test():
    return {"message": "API is working!"}

# Vercel 需要这个
app = app.wsgi_app
