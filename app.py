from flask import Flask, request, jsonify
from flask_oauthlib.provider import OAuth2Provider
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from DataBase import session, FileData
import textract

app = Flask(__name__)
oauth = OAuth2Provider(app)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file provided", 400
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
    content = extract_text(file)
    file_data = FileData(filename=file.filename, content=content)
    session.add(file_data)
    session.commit()
    return "File uploaded successfully"

def extract_text(file):
    content = ""
    if file.filename.endswith('.txt'):
        content = file.read().decode('utf-8')
    elif file.filename.endswith('.csv'):
        content = file.read().decode('utf-8')
    elif file.filename.endswith('.pdf'):
        content = textract.process(file)
    elif file.filename.endswith(('.doc', '.docx', '.ppt', '.pptx')):
        content = textract.process(file, method='pdftotext')  
    
    return content


@app.route('/files', methods=['GET'])
def get_files():
    files = session.query(FileData).all()
    data = [{'filename': file.filename, 'content': file.content} for file in files]
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)