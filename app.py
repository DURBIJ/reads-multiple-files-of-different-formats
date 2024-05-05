from flask import Flask, request, jsonify
from flask_oauthlib.provider import OAuth2Provider
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from DataBase import session, FileData
from uploadFiles import upload
from get_db_data import get_files
from authentication import authenticate

app = Flask(__name__)
oauth = OAuth2Provider(app)


@app.route('/upload', methods=['POST'])
@authenticate
def upload_file():
    return upload()


@app.route('/files', methods=['GET'])
@authenticate
def get_files_data():
    return get_files()


if __name__ == '__main__':
    app.run(debug=True)