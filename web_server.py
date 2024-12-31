from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-key-123')

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/test')
def test():
    return "Server is working!"

if __name__ == '__main__':
    app.run(debug=True)