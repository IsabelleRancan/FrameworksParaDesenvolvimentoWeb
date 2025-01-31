from datetime import datetime 

USERNAME = "IsabelleRancan"
PASSWORD = "1234"   

def greeting_message():
    time = datetime.now().hour 

    if time < 12: 
        return "Good morning!"
    elif time < 18:
        return "Good afternoon!"
    else: 
        return "Good night!"
    
    
def authenticate_user(username, password):
    return username == USERNAME and password==PASSWORD



