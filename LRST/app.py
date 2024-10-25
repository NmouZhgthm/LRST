from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Vercel 需要这个
app.debug = True

# 修改入口点
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
