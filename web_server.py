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

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/auth/twitter')
def twitter_auth():
    try:
        redirect_uri = url_for('twitter_callback', _external=True)
        return oauth.twitter.authorize_redirect(redirect_uri)
    except Exception as e:
        print(f"Twitter auth error: {str(e)}")
        return jsonify({"success": False, "message": str(e)})

@app.route('/callback')
def twitter_callback():
    try:
        token = oauth.twitter.authorize_access_token()
        session['twitter_token'] = token
        return redirect('/tasks')
    except Exception as e:
        print(f"Callback error: {str(e)}")
        return str(e), 500

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    if 'twitter_token' not in session:
        return jsonify({"success": False, "message": "Not authenticated"})
    
    try:
        # Ici vous pouvez ajouter la logique de vérification
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)