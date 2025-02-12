import os
from datetime import datetime 
from flask import current_app 

UPLOAD_PICTURES = "/static/img/upload_pictures"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_files(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file):
    if file and allowed_files(file.filename):
        timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
        filename = f"{timestamp}_{file.filename}"
        filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
        return filepath
    return None 