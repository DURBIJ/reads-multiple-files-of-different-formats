from flask import Flask, request
from flask_oauthlib.provider import OAuth2Provider
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import textract

app = Flask(__name__)
oauth = OAuth2Provider(app)

# Database Setup
engine = create_engine('sqlite:///data.db')
Base = declarative_base()

class FileData(Base):
    __tablename__ = 'file_data'
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    content = Column(Text)

# create database tables based 
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


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
    return content


if __name__ == '__main__':
    app.run(debug=True)