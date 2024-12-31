from flask import Flask, render_template, jsonify
from flask_cors import CORS
import tweepy

app = Flask(__name__)
CORS(app)

# Configuration Twitter API
auth = tweepy.OAuthHandler("YOUR_CONSUMER_KEY", "YOUR_CONSUMER_SECRET")
auth.set_access_token("YOUR_ACCESS_TOKEN", "YOUR_ACCESS_TOKEN_SECRET")
api = tweepy.API(auth)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/verify-twitter-follow', methods=['POST'])
def verify_twitter_follow():
    try:
        # Vérifier si l'utilisateur suit @EngageVault
        friendship = api.get_friendship(source_screen_name="USER_SCREEN_NAME", 
                                     target_screen_name="EngageVault")
        
        if friendship[0].following:
            # Ici, vous ajouteriez la logique pour attribuer les points
            return jsonify({"success": True})
        else:
            return jsonify({"success": False})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)