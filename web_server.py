from flask import Flask, render_template, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    print("Main route accessed")  # Pour le débogage
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)