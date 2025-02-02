from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from .form import greeting_message, authenticate_user
from .generate_form import generate_form, process_json_to_list
from .authentication_user import User
from .full_form import user_authenticate
from datetime import timedelta, datetime
import os

app = Flask(__name__)
app.secret_key = "840d5791054e889b8ab0cdf7b14190ea"

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
        {"name": "1 - Crie uma rota para uma página web com a tag canvas que permite ao usuário deslocar uma fotografia para a direita e esquerda com as setinhas do teclado.", "url": url_for("activity", activity_id="list01", activity_name="ex01")},
        {"name": "2 - Crie uma rota que permita ao usuário capturar uma fotografia pela webcam e mostrar na tela.", "url": url_for("activity", activity_id="list01", activity_name="ex02")},
        {"name": "3 - Crie uma rota que exiba uma tabela (sem usar table) com 997 linhas e 5 colunas: nas colunas id, nome, sobre nome, email, ações", "url": url_for("activity", activity_id="list01", activity_name="ex03")},
        {"name": "4 - Criar uma rota com 3 links, um para cada uma das atividades anteriores, porém todas elas bonitas", "url": url_for("activity", activity_id="list01", activity_name="ex04")},
        {"name": "5 - Criar rotas contendo o curriculo de cada um dos integrantes do grupo (estilizado).", "url": url_for("activity", activity_id="list01", activity_name="ex05")},
    ]

    list02 = [
        {"name": "1 - Considerando um usuário e uma senha mocados (dados fictícios) faça uma página de autenticação que retorne uma mensagem caso a autenticação funcionar (bom dia, tarde, noite a depender do horário), se não, diz que o login não bateu.", "url": url_for("activity", activity_id="list02", activity_name="ex01")},
        {"name": "2 - Gerando um arquivo html com um formulário de forma automática", "url": url_for("activity", activity_id="list02", activity_name="ex02")},
        {"name": "3 - Formulário com autenticação de usuário", "url": url_for("activity", activity_id="list02", activity_name="ex03")},
    ]

    list03 = [
        {"name": "1 - Formulário completo com dados mokados, autenticação, limitação de tentativas de login e tratar exceções.", "url": url_for("activity", activity_id="list03", activity_name="ex01")},
    ]
    
    list04 = [
        {"name": "1 - Mini Blog Pessoal", "url": url_for("activity", activity_id="list04", activity_name="ex01")},
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
    error = request.args.get("error", None)  # Pegando erro da URL, se existir
    validator = request.args.get("validator", None)  # Pegando validação bem-sucedida
    
    if request.method == "POST":
        name = request.form["name"]
        lastname = request.form["lastname"]
        age = int(request.form["age"])
        email = request.form["email"]
        password = request.form["password"]

        try: 
            User(name, lastname, age, email, password)
            return redirect(url_for("user_data", error="Welcome to login"))  # Redireciona corretamente
        except ValueError as e:
            return redirect(url_for("user_data", error=str(e)))  # Redireciona com erro
    
    return render_template("list02/ex03.html", error=error, validator=validator)


@app.route("/activity/list02/ex03-validation", methods=["POST"])
def validation():
    email = request.form["email"]
    password = request.form["password"]

    try: 
        User.login_user(email, password)
        return redirect(url_for("user_data", validator="Welcome"))  # Redireciona com sucesso
    except ValueError as e:
        return redirect(url_for("user_data", error=str(e)))  # Redireciona com erro

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

@app.route("/activity/list04/ex01/new_post", methods=["GET", "POST"])
def new_post():
    posts = []

    if request.method == "POST":
        text = request.form["text"]
        date = datetime.now()
        time = datetime.now()

        posts.append({"text": text, "date": date, "time": time})
        return render_template("list04/ex01.html", posts=posts)
    return render_template("list04/ex01_new_post.html")