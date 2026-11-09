# lab2_bruteforce/app_secure.py
from flask import Flask, request, render_template_string, session, redirect, url_for
import time
from collections import defaultdict

app = Flask(__name__)
app.secret_key = "dev-key"

# Demo user database (do not use plaintext in production)
USERS = {"alice": "wonderland", "bob": "builder", "carol": "1234"}

TEMPLATE = """
<h2>Lab 2 - Brute Force Login Demo (PATCHED)</h2>
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

# Simple in-memory tracking (lab/demo only)
FAILED_ATTEMPTS_USER = defaultdict(int)
FAILED_ATTEMPTS_IP = defaultdict(int)
LOCKED_UNTIL = {}

# Config for demo
MAX_FAILED_USER = 5
LOCK_SECONDS = 60    # lock for 60 seconds after threshold
SLOWDOWN_AFTER = 3   # add small delay per-IP after this

def get_ip():
    return request.remote_addr or 'unknown'

@app.before_request
def cleanup_locks():
    now = time.time()
    expired = [u for u, t in LOCKED_UNTIL.items() if t <= now]
    for u in expired:
        del LOCKED_UNTIL[u]

@app.route("/", methods=["GET", "POST"])
def login():
    message = None
    ip = get_ip()
    if request.method == "POST":
        user = request.form.get("user", "")
        password = request.form.get("password", "")

        if user in LOCKED_UNTIL:
            message = f"Account locked until {time.ctime(LOCKED_UNTIL[user])}."
            return render_template_string(TEMPLATE, message=message)

        valid = user in USERS and USERS[user] == password
        if valid:
            FAILED_ATTEMPTS_USER[user] = 0
            FAILED_ATTEMPTS_IP[ip] = 0
            session["user"] = user
            return redirect(url_for("secret"))
        else:
            FAILED_ATTEMPTS_USER[user] += 1
            FAILED_ATTEMPTS_IP[ip] += 1

            if FAILED_ATTEMPTS_USER[user] >= MAX_FAILED_USER:
                LOCKED_UNTIL[user] = time.time() + LOCK_SECONDS
                message = "Too many failed attempts; account temporarily locked."
            else:
                message = "Invalid username or password."

            if FAILED_ATTEMPTS_IP[ip] >= SLOWDOWN_AFTER:
                delay = min(5, FAILED_ATTEMPTS_IP[ip] - SLOWDOWN_AFTER + 1)
                time.sleep(delay)  # small demo slowdown

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
