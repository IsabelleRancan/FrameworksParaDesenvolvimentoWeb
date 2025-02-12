import os
from datetime import datetime
from flask import current_app, request
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
        filename = f"{timestamp}_{filename}"
        

        if "VERCEL" in os.environ:
            return f"Unable to generate files or folders, try running the local version of this application."  # Exemplo para URL de um serviço externo
        

        upload_folder = "uploads"
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        return filepath
    return None
