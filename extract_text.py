import textract

def extract_file_text(file):
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
