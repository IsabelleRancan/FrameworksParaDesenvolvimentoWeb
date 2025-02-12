import os
from datetime import datetime 
from flask import current_app 

UPLOAD_PICTURES = "/tmp/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

if not os.path.exists(UPLOAD_PICTURES):
    os.makedirs(UPLOAD_PICTURES)

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