from flask import Flask, render_template, jsonify, session, redirect, url_for
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-key-123')

oauth = OAuth(app)
oauth.register(
    name='twitter',
    client_id=os.environ.get('TWITTER_CLIENT_ID'),
    client_secret=os.environ.get('TWITTER_CLIENT_SECRET'),
    api_base_url='https://api.twitter.com/2/',
    access_token_url='https://api.twitter.com/2/oauth2/token',
    authorize_url='https://twitter.com/i/oauth2/authorize',
    client_kwargs={'scope': 'tweet.read users.read follows.read'}
)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/test')
def test():
    return "Server is working!"

if __name__ == '__main__':
    app.run(debug=True)