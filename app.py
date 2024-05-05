from flask import Flask, request, jsonify
from flask_oauthlib.provider import OAuth2Provider
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from DataBase import session, FileData
from uploadFiles import upload

app = Flask(__name__)
oauth = OAuth2Provider(app)


@app.route('/upload', methods=['POST'])
def upload_file():
    return upload()


@app.route('/files', methods=['GET'])
def get_files():
    files = session.query(FileData).all()
    data = [{'filename': file.filename, 'content': file.content} for file in files]
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)