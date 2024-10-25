from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Vercel 需要这个处理程序
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

# 确保这样写
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
