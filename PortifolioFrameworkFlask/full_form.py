import re

USERNAME = "IsabelleRancan"
PASSWORD = "1234"  

def validate_credentials(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        return "Invalid input type."
    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        return "Invalid username format. Only letters, numbers, and underscore are allowed."
    if not password.isdigit():
        return "Invalid password format. Password must contain only numbers."
    return None

def user_authenticate(username, password):
    error = validate_credentials(username, password)
    if error:
        return error
    return "Success" if username == USERNAME and password==PASSWORD else "Incorrect username or password"