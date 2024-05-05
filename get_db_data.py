from flask import jsonify
from DataBase import session, FileData

def get_files():
    files = session.query(FileData).all()
    data = [{'filename': file.filename, 'content': file.content} for file in files]
    return jsonify(data)