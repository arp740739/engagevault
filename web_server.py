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
    scope=["tweet.read", "users.read", "follows.read"]
)

@app.route('/login')
def login():
    return redirect(oauth2_client.get_authorization_url())

@app.route('/callback')
def callback():
    try:
        code = request.args.get('code')
        token = oauth2_client.fetch_token(code)
        session['token'] = token
        return redirect('/main')
    except Exception as e:
        print(f"Callback error: {str(e)}")
        return redirect('/')

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    if 'token' not in session:
        return jsonify({
            "success": False,
            "message": "Please login with Twitter first",
            "redirect": "/login"
        })

    try:
        # Utiliser le token de l'utilisateur
        client = tweepy.Client(session['token']['access_token'])
        
        print("Starting verification...")  # Log de débogage
        
        try:
            # Obtenir l'ID de l'utilisateur connecté
            me = client.get_me()
            user_id = me.data.id
            
            # Vérifier si l'utilisateur suit @EngageVault
            target_id = "1874098225139113984"  # ID de @EngageVault
            
            following = client.get_users_following(user_id)
            if following and following.data:
                following_ids = [user.id for user in following.data]
                if int(target_id) in following_ids:
                    return jsonify({
                        "success": True,
                        "message": "Congratulations! You earned 50 points!",
                        "points": 50
                    })
            
            return jsonify({
                "success": False,
                "message": "You need to follow @EngageVault first!"
            })
                
        except Exception as e:
            print(f"Twitter API Error: {str(e)}")
            return jsonify({
                "success": False,
                "message": "Error checking follow status"
            })
            
    except Exception as e:
        print(f"Server Error: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Server error. Please try again."
        })

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)