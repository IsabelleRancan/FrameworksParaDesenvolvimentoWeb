import os
from datetime import datetime 
from flask import current_app 

UPLOAD_PICTURES = "/static/img/upload_pictures"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

if not os.path.exists(UPLOAD_PICTURES):
    os.makedirs(UPLOAD_PICTURES)

def allowed_files(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file):
    if file and allowed_files(file.filename):
        timestamp = datetime.now().strftime("%y%m%d_%h%m%s")
        filename = f"{timestamp}_{file.filename}"
        filepath = os.path.join(current_app.config[UPLOAD_PICTURES], filename)
        #filepath = os.path.join(UPLOAD_PICTURES, filename)
        file.save(filepath)
        return filepath
    return None 