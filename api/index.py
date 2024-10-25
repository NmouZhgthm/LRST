from flask import Flask, render_template
import os

app = Flask(__name__, 
    template_folder='../templates',
    static_folder='../static'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/test')
def test():
    return {"message": "API is working!"}

if __name__ == '__main__':
    app.run()
