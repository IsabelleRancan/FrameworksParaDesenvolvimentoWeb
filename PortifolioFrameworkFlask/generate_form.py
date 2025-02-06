import os

def generate_form(directory, filename):
    form = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="../../static/css/style.css">
            <link rel= "icon" href="../../static/img/app/sparkles.png">
            <title>Exercise 2</title>
        </head>
        <body>
            
        <div class="form">
            <h1>Generated Form</h1>

            <form method="POST" action="/activity/list02/ex02-processing">
                <label for="username">Username</label>
                <input type="text" name="username" id="username" required><br><br>
                <label for="password">Password</label>
                <input type="password" name="password" id="password" required><br><br>
                <button type="submit">Send</button>
            </form>
        </div>

        </body>
        </html>
    '''

    if not os.path.exists(directory):
        os.makedirs(directory)

    filepath = os.path.join(directory, filename)
    print(f"{filepath}")

    with open(filepath, 'w') as file:
        file.write(form)

def process_json_to_list(json_data):
    result_list = []
    for key, value in json_data.items():
        result_list.append({key: value, key: value})
    return result_list
