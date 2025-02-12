# Portfólio Framework Flask

This project was developed using the Flask framework to create dynamic web applications. The project includes several routes that explore functionalities such as image manipulation on a canvas, displaying tables, and interacting with dynamic data.

## Technologies Used
- **Python 3**
- **Flask**
- **HTML, CSS, and JavaScript**
- **SCSS** (for styling)

## Project Structure

```
FrameworksParaDesenvolvimentoWeb/
│── PortifolioFrameworkFlask/
│   │── static/
│   │   │── css/
│   │   │   │── style.css
│   │   │   │── style.css.map
│   │   │   │── style.scss
│   │   │── img/
│   │   │   │── app/
│   │   │       │── car.png
│   │   │       │── envelope-solid-24.png
│   │   │       │── github-logo-24.png
│   │   │       │── linkedin-square-logo-24.png
│   │   │       │── sparkles.png
│   │   │       │── whatsapp-square-logo-24.png
│   │   │── js/
│   │   │   │── list01/
│   │   │       │── script01.js
│   │   │       │── script02.js
│   │   │       │── script03.js
│   │── templates/
│   │   │── list01/
│   │   │   │── ex01.html
│   │   │   │── ex02.html
│   │   │   │── ex03.html
│   │   │   │── ex04.html
│   │   │   │── ex05.html
│   │   │   │── ex06.html
│   │   │   │── ex07.html
│   │   │   │── ex08.html
│   │   │   │── ex09.html
│   │   │   │── ex10.html
│   │   │── list02/
│   │   │   │── ex01.html
│   │   │   │── ex02.html
│   │   │   │── ex03.html
│   │   │── list03/
│   │   │   │── ex01.html
│   │   │── list04/
│   │   │   │── ex01.html
│   │   │   │── ex01_new_post.html
│   │   │   │── ex02.html
│   │   │   │── ex02_login.html
│   │   │   │── ex03.html
│   │   │── index.html
│   │   │── navbar.html
│   │── __init__.py
│   │── authentication_user.py
│   │── basic_authentication_page.py
│   │── form.py
│   │── full_form.py
│   │── generate_form.py
│   │── upload_pictures.py
│── main.py
│── requirements.txt
│── README.md

```

## Installation and Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/IsabelleRancan/FrameworksParaDesenvolvimentoWeb.git
   cd your-repository
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```
5. Access it in the browser:
   ```
   http://127.0.0.1:5000
   ```

## Features
- **Interactive Canvas**: A route that allows you to move images using the keyboard keys.
- **Dynamic Form Generator**: Automatically generates and saves forms.
- **JSON Integration**: Conversion and processing of data.

## Deployment
The project has been deployed on Vercel and can be accessed through the following link: < >

---
Developed by Isabelle Firmino Rancan