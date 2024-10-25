from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from LRST!"

@app.route('/api/test')
def test():
    return {"message": "API is working!"}

if __name__ == '__main__':
    app.run()
