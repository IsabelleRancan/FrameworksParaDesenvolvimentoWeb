from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from .form import greeting_message, authenticate_user
from .generate_form import generate_form, process_json_to_list
from .authentication_user import User
from .full_form import user_authenticate
from datetime import timedelta, datetime
from .upload_pictures import allowed_files, save_file
from .basic_authentication_page import Create_User
import os

app = Flask(__name__)
app.secret_key = "840d5791054e889b8ab0cdf7b14190ea"
app.config["UPLOAD_FOLDER"] = "/static/img/upload_pictures"

if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

def generate_html_if_needed():
    base_path = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(base_path, "templates", "list02")
    filename = "ex02.html"

    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(os.path.join(directory, filename)):
        generate_form(directory, filename)

generate_html_if_needed()

@app.route("/")
def index():
    list01 = [
        {"name": "1.	Create a route for a web page containing a <canvas> tag that allows users to move an image left and right using the keyboard arrow keys.", "url": url_for("activity", activity_id="list01", activity_name="ex01")},
        {"name": "2.	Create a route for Activity 2 that allows the user to capture an image using the webcam and display it on the screen.", "url": url_for("activity", activity_id="list01", activity_name="ex02")},
        {"name": "3.	Create a route for Activity 3 that displays a table (without using <table>) containing 997 rows and 5 columns (id, first name, last name, email, actions).", "url": url_for("activity", activity_id="list01", activity_name="ex03")},
        {"name": "4.	Create a route with 3 links, each leading to one of the previous activities, ensuring they all have a beautiful design.", "url": url_for("activity", activity_id="list01", activity_name="ex04")},
        {"name": "5.	Create 6 routes, each styled and well-designed, with each route containing the resume of a different group member.", "url": url_for("activity", activity_id="list01", activity_name="ex05")},
    ]

    list02 = [
        {"name": "1.	Create an authentication page considering a mock username and password. The page should return a personalized message depending on the time of day, limit the login attempts to a maximum of 2 attempts, and style the login page to be visually appealing.", "url": url_for("activity", activity_id="list02", activity_name="ex01")},
        {"name": "2.	Write a Python script that automatically generates an HTML template containing a form for data input with fields that will be received via JSON. Build an automatic route to allow viewing it.", "url": url_for("activity", activity_id="list02", activity_name="ex02")},
        {"name": "3.	Create a Python class to encapsulate user data.  Develop an authentication function that validates user credentials and create a session to store and authenticate the user.", "url": url_for("activity", activity_id="list02", activity_name="ex03")},
    ]

    list03 = [
        {"name": "1.	Complete form with mock data, authentication, login attempt limitation, and exception handling.", "url": url_for("activity", activity_id="list03", activity_name="ex01")},
    ]
    
    list04 = [
        {"name": "1.	Personal mini-blog.", "url": url_for("activity", activity_id="list04", activity_name="ex01")},
        {"name": "2.	Basic authentication page.", "url": url_for("activity", activity_id="list04", activity_name="ex02")},
        {"name": "3.	Photo upload page.", "url": url_for("activity", activity_id="list04", activity_name="ex03")},
    ]

    return render_template("index.html", list01=list01, list02=list02, list03=list03, list04=list04)

@app.route("/activity/<activity_id>/<activity_name>")
def activity(activity_id, activity_name):
    return render_template(f"{activity_id}/{activity_name}.html")

@app.route("/activity/list02/ex01", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        session.pop("login_attempts", None)

    error = None
    
    if request.method == "POST":
        if "login_attempts" not in session:
            session["login_attempts"] = 0
        session["login_attempts"] += 1

        if session["login_attempts"] >= 2:
            error = "Maximum number of login attempts reached"
        else: 
            username = request.form["username"]
            password = request.form["password"]

            if authenticate_user(username, password):
                session.pop("login_attempts", None)
                message = greeting_message()
                return render_template("list02/ex01.html", message=message)
            else:
                error = "Incorrect username or password"
    
    return render_template("list02/ex01.html", error=error)

@app.route("/activity/list02/ex02-processing", methods=["POST"])
def processing():
    data = request.form.to_dict(flat=True)

    result_list = process_json_to_list(data)
    return jsonify(result_list)

@app.route("/activity/list02/ex03", methods=["GET", "POST"])
def user_data():
    error = request.args.get("error", None) 
    validator = request.args.get("validator", None) 
    
    if request.method == "POST":
        name = request.form["name"]
        lastname = request.form["lastname"]
        age = int(request.form["age"])
        email = request.form["email"]
        password = request.form["password"]

        try: 
            User(name, lastname, age, email, password)
            return redirect(url_for("user_data", error="Welcome to login")) 
        except ValueError as e:
            return redirect(url_for("user_data", error=str(e))) 
    
    return render_template("list02/ex03.html", error=error, validator=validator)


@app.route("/activity/list02/ex03-validation", methods=["POST"])
def validation():
    email = request.form["email"]
    password = request.form["password"]

    try: 
        User.login_user(email, password)
        return redirect(url_for("user_data", validator="Welcome"))  
    except ValueError as e:
        return redirect(url_for("user_data", error=str(e))) 

@app.route("/activity/list03/ex01", methods=["GET", "POST"])
def form_login():

    if request.method == "GET":
        session.pop("login_attempts", None)

    error = None
    message = None      
    
    if request.method == "POST":
        if "login_attempts" not in session:
            session["login_attempts"] = 0
        session["login_attempts"] += 1

        if session["login_attempts"] >= 2:
            error = "Maximum number of login attempts reached"
        else: 
            username = request.form["username"]
            password = request.form["password"]

            result = user_authenticate(username, password)

            if result == "Success":
                session.pop("login_attempts", None)
                message="Login successfully!!"
            else:
                error = result

    return render_template("list03/ex01.html", error=error, message=message)

posts = []
@app.route("/activity/list04/ex01/new_post", methods=["GET", "POST"])
def new_post():
    global posts

    if request.method == "POST":
        text = request.form["text"]
        date = datetime.now().strftime("%d/%m/%y")
        time = datetime.now().strftime("%H:%M")

        posts.append({"text": text, "date": date, "time": time})
        return render_template("list04/ex01.html", posts=posts)
    return render_template("list04/ex01_new_post.html")

@app.route("/activity/list04/ex03/upload_pictures", methods=["GET", "POST"])
def pictures():
    message = None 
    filepath = None

    if request.method == "POST": 
        if "file" not in request.files:
            return render_template("list04/ex03.html", message="No file part", filepath=filepath)
        
        file = request.files["file"]
        if file.filename == "":
            return render_template("list04/ex03.html", message="No selected file", filepath=filepath)
        
        filepath = save_file(file)
        if filepath: 
            return render_template("list04/ex03.html", message="Success", filepath=filepath)
        else:
            return render_template("list04/ex03.html", message="Invalid file format", filepath=filepath)
        
    return render_template("list04/ex03.html")

@app.route("/activity/list04/ex02/create_account", methods=["GET", "POST"])
def create_account():
    error = None  
    
    if request.method == "POST":
        name = request.form["name"]
        lastname = request.form["lastname"]
        age = int(request.form["age"])
        email = request.form["email"]
        password = request.form["password"]

        try: 
            Create_User(name, lastname, age, email, password)
            return render_template("list04/ex02_login.html")
        except ValueError as e:
            return redirect(url_for("user_data", error=str(e)))
    
    return render_template("list04/ex02.html", error=error)

@app.route("/activity/list04/ex02_login", methods=["POST"])
def user_login():
    email = request.form["email"]
    password = request.form["password"]

    try: 
        Create_User.login_users(email, password)
        return render_template("list04/ex02_login.html", validator="Welcome")
    except ValueError as e:
        return render_template("list04/ex02_login.html", error=str(e))