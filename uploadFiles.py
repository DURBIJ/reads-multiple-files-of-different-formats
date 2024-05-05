from flask import jsonify,request
from DataBase import session, FileData
from extract_text import extract_file_text

def upload():
    if 'file' not in request.files:
        return "No file provided", 400
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
    content = extract_file_text(file)
    file_data = FileData(filename=file.filename, content=content)
    session.add(file_data)
    session.commit()
    return "File uploaded successfully"

