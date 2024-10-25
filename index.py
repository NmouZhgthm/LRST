from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, LRST!"  # 先用简单的返回测试

if __name__ == '__main__':
    app.run()
