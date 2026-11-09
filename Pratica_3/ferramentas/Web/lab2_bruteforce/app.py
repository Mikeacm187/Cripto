from flask import Flask, request, render_template_string, session, redirect, url_for
from time import sleep

app = Flask(__name__)
app.secret_key = "dev-key"

# Demo user database
USERS = {"alice": "wonderland", "bob": "builder", "carol": "1234"}

TEMPLATE = """
<h2>Lab 2 – Brute Force Login Demo</h2>
{% if message %}<p style='color:red;'>{{message}}</p>{% endif %}
<form method="post">
  Username: <input name="user"><br>
  Password: <input name="password" type="password"><br>
  <button type="submit">Login</button>
</form>
{% if session.get('user') %}
<p>You are logged in as {{session['user']}}. <a href="/logout">Logout</a></p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = None
    if request.method == "POST":
        user = request.form.get("user", "")
        password = request.form.get("password", "")
        if user in USERS and USERS[user] == password:
            session["user"] = user
            return redirect(url_for("secret"))
        else:
            message = "Invalid username or password."
    return render_template_string(TEMPLATE, message=message)

@app.route("/secret")
def secret():
    if "user" not in session:
        return redirect(url_for("login"))
    return f"<h3>Welcome, {session['user']}!</h3><p>Here is your secret data!</p>"

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
