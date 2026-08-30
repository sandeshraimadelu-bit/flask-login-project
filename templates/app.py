from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    if email == "admin@gmail.com" and password == "1234":
        return "<h2>Login Successful!</h2>"
    else:
        return "<h2>Invalid Email or Password!</h2>"

if __name__ == "__main__":
    app.run(debug=True)