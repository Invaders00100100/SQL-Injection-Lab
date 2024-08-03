import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML content for the main page
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SQL Injection Vulnerability Example</title>
    <style>
        body {
            color: violet;
            font-family: Arial, sans-serif;
            background-color: #121212;
            margin: 0;
            padding: 20px;
        }
        .content {
            max-width: 800px;
            margin: auto;
            background: #1e1e1e;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px 0;
        }
        a {
            color: #bb86fc;
        }
        pre {
            background: #2d2d2d;
            color: #d4d4d4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        .comment {
            color: #bb86fc;
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>SQL Injection Vulnerability Example</h1>
        <p>The following Login Page is vulnerable to SQL injection due to the way it constructs the SQL query using string concatenation with user input. The query is built by embedding the username and password directly into the SQL string without any form of sanitization or escaping.</p>
        
        <pre><span class="comment"># This is the vulnerable part of the code</span>
conn = sqlite3.connect('testdb.sqlite')
cursor = conn.cursor()
query = f"SELECT * FROM users WHERE username = '{{username}}' AND password = '{{password}}'"
cursor.execute(query)
result = cursor.fetchall()
conn.close()
        </pre>
        
        <pre><span class="comment"># This is the secure version of the above which uses parameterized queries</span>
conn = sqlite3.connect('testdb.sqlite')
cursor = conn.cursor()
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
result = cursor.fetchall()
conn.close()
        </pre>

        <img src="https://www.redeweb.com/wp-content/uploads/2021/03/software-1.jpg" alt="Software Image">

        <p><a href="/login">Go to the vulnerable app</a></p>
    </div>
</body>
</html>
"""

# Route for the main page
@app.route('/')
def index():
    return html_content

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('testdb.sqlite')
        cursor = conn.cursor()
        
        # Vulnerable query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchall()
        
        conn.close()
        
        if result:
            return render_template_string('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Login Successful</title>
                <style>
                    body {
                        background-color: #121212;
                        color: #ffffff;
                        font-family: Arial, sans-serif;
                        text-align: center;
                        padding: 50px;
                    }
                    img {
                        max-width: 100%;
                        height: auto;
                    }
                </style>
            </head>
            <body>
                <h1>Login Successful</h1>
                <img src="https://t3.ftcdn.net/jpg/03/77/78/18/360_F_377781834_GEkkTCjThmPqxd7FZPLF6FNnPDOcG1yM.jpg" alt="Success Image">
            </body>
            </html>
            ''')
        else:
            return render_template_string('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Login Failed</title>
                <style>
                    body {
                        background-color: #121212;
                        color: #ffffff;
                        font-family: Arial, sans-serif;
                        text-align: center;
                        padding: 50px;
                    }
                    img {
                        max-width: 100%;
                        height: auto;
                    }
                </style>
            </head>
            <body>
                <h1>Login Failed</h1>
                <img src="https://t4.ftcdn.net/jpg/03/77/78/17/360_F_377781792_j2jOYENO4CDuw9Y6rmioE1yfE1X5L3sv.jpg" alt="Failure Image">
            </body>
            </html>
            ''')
    
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Page</title>
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style type="text/css">
            * {
                padding: 0;
                margin: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Poppins', sans-serif;
                background-color: #1e1e1e;
                color: #ffffff;
            }

            main {
                height: 70vh;
                width: 100vw;
                position: relative;
                margin: 0 auto;
            }

            footer {
                height: 30vh;
                background-color: #121212;
            }

            .row {
                display: flex;
                justify-content: space-around;
                align-items: center;
                width: 100%;
                max-width: 1000px;
                position: absolute;
                left: 50%;
                top: 50%;
                transform: translate(-50%, -50%);
            }

            .col-logo {
                flex: 0 0 50%;
                text-align: left;
            }

            .col-form {
                flex: 0 0 40%;
                text-align: center;
            }

            .col-logo img {
                max-width: 300px;
            }

            .col-logo h2 {
                font-size: 26px;
                font-weight: 400;
                padding: 0 30px;
                line-height: 32px;
                color: #32CD32; /* Lime green color */
            }

            .col-form .form-container {
                background-color: #2e2e2e;
                border: none;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.1);
                margin-bottom: 30px;
                padding: 20px;
                max-width: 400px;
            }

            .col-form .form-container input,
            .col-form .form-container .btn-login {
                width: 100%;
                margin: 5px 0;
                height: 45px;
                vertical-align: middle;
                font-size: 16px;
            }

            .col-form .form-container input {
                border: 1px solid #dddfe2;
                color: #1d2129;
                padding: 0 8px;
                outline: none;
            }

            .col-form .form-container input:focus {
                border-color: #1877f2;
                box-shadow: 0 0 0 2px #e7f3ff;
            }

            .col-form .form-container .btn-login {
                background-color: #32CD32; /* Lime green color */
                border: none;
                border-radius: 6px;
                font-size: 20px;
                padding: 0 16px;
                color: #ffffff;
                font-weight: 700;
            }

            .col-form .form-container a {
                display: block;
                color: #1877f2;
                font-size: 14px;
                text-decoration: none;
                padding: 10px 0 20px;
                border-bottom: 1px solid #dadde1;
            }

            .col-form .form-container a:hover {
                text-decoration: underline;
            }

            .col-form .form-container .btn-new {
                background-color: #42b72a;
                border: none;
                border-radius: 6px;
                font-size: 17px;
                line-height: 48px;
                padding: 0 16px;
                color: #ffffff;
                font-weight: 700;
                margin-top: 20px;
            }

            .col-form p {
                font-size: 14px;
            }

            .col-form p a {
                text-decoration: none;
                color: #1c1e21;
                font-weight: 600;
            }

            .col-form p a:hover {
                text-decoration: underline;
            }

            .footer-contents {
                position: relative;
                max-width: 1000px;
                margin: 0 auto;
            }

            footer ol {
                display: flex;
                flex-wrap: wrap;
                list-style-type: none;
                padding: 10px 0;
            }

            footer ol:first-child {
                border-bottom: 1px solid #dddfe2;
            }

            footer ol:first-child li:last-child button {
                background-color: #f5f6f7;
                border: 1px solid #ccd0d5;
                outline: none;
                color: #4b4f56;
                padding: 0 8px;
                font-weight: 700;
                font-size: 16px;
            }

            footer ol li {
                padding-right: 15px;
                font-size: 12px;
                color: #385898;
            }

            footer ol li a {
                text-decoration: none;
                color: #385898;
            }

            footer ol li a:hover {
                text-decoration: underline;
            }

            footer small {
                font-size: 11px;
                color: #dddfe2;
            }

            .vulnerability-message {
                margin-bottom: 20px;
                font-size: 16px;
                color: #EE82EE; /* Violet color */
                text-align: center;
                padding: 10px;
                border: 1px solid #EE82EE;
                border-radius: 5px;
                background-color: #2e2e2e;
                max-width: 400px;
                margin: 20px auto;
            }
        </style>
    </head>

    <body>
        <main>
            <div class="row">
                <div class="col-logo">
                    <img src="https://as2.ftcdn.net/v2/jpg/05/56/95/23/1000_F_556952350_wzRxRFaq651sOsBVi8JAMfgEDKfLI6Vz.jpg" alt="Login Image">
                    <h2>Craft an SQL payload to bypass authentication to gain unauthorized access</h2>
                </div>
                <div class="col-form">
                    <form method="post" action="/login" class="form-container">
                        <input type="text" name="username" placeholder="Username"><br>
                        <input type="password" name="password" placeholder="Password"><br><br>
                        <input type="submit" value="Login" class="btn-login">
                    </form>
                </div>
            </div>
        </main>
        <footer>
            <div class="footer-contents">
                <small>Invader-Productions © 2024</small>
            </div>
        </footer>
    </body>

    </html>
    ''')

# Creating the database and adding a user
def init_db():
    conn = sqlite3.connect('testdb.sqlite')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', 'password123'))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
