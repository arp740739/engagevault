from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from EngageVault!"

# Ne pas inclure cette partie pour le déploiement
# if __name__ == '__main__':
#     app.run()