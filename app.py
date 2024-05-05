from flask import Flask
from flask_oauthlib.provider import OAuth2Provider


app = Flask(__name__)
oauth = OAuth2Provider(app)

if __name__ == '__main__':
    app.run(debug=True)