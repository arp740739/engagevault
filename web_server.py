from flask import Flask, render_template, jsonify, redirect, session, request
from flask_cors import CORS
import tweepy
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
CORS(app)

# Configuration OAuth 2.0
oauth2_client = tweepy.OAuth2UserHandler(
    client_id=os.getenv('TWITTER_CLIENT_ID'),
    client_secret=os.getenv('TWITTER_CLIENT_SECRET'),
    redirect_uri="https://engagevault.onrender.com/callback",
    scope=["tweet.read", "users.read"]
)

@app.route('/auth/twitter')
def twitter_auth():
    try:
        auth_url = oauth2_client.get_authorization_url()
        session['oauth_state'] = oauth2_client.state
        return jsonify({
            "success": True,
            "auth_url": auth_url
        })
    except Exception as e:
        print(f"Auth Error: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error initiating authentication"
        })

@app.route('/callback')
def callback():
    try:
        code = request.args.get('code')
        state = request.args.get('state')
        
        if state != session.get('oauth_state'):
            return redirect('/main?error=invalid_state')
            
        token = oauth2_client.fetch_token(code)
        session['twitter_token'] = token
        
        return redirect('/main?success=true')
        
    except Exception as e:
        print(f"Callback Error: {str(e)}")
        return redirect('/main?error=auth_failed')

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    if 'twitter_token' not in session:
        return jsonify({
            "success": False,
            "message": "Please connect your X account first"
        })
        
    try:
        # Vérifier que le token est valide
        client = tweepy.Client(session['twitter_token']['access_token'])
        me = client.get_me()
        
        if me:
            return jsonify({
                "success": True,
                "message": "Congratulations! Account linked successfully!",
                "points": 50
            })
        else:
            return jsonify({
                "success": False,
                "message": "Could not verify X account"
            })
            
    except Exception as e:
        print(f"Verification Error: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error verifying X account"
        })

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)