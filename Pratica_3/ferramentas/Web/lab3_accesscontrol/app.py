from flask import Flask, session, request, redirect, url_for, render_template_string, abort

app = Flask(__name__)
app.secret_key = "dev-key"

# Demo data: each user's private notes
DATA = {
    "alice": {"note": "Alice’s confidential report"},
    "bob": {"note": "Bob’s private schedule"},
}

USERS = {"alice": "a", "bob": "b", "admin": "root"}

PAGE = """
<h2>Lab 3 – Access Control / IDOR</h2>
{% if user %}
  <p>Logged in as {{user}} (<a href="/logout">logout</a>)</p>
  <p>View your data: <a href="/profile?user={{user}}">/profile?user={{user}}</a></p>
  <p>Try: <code>/profile?user=alice</code> or <code>/profile?user=bob</code></p>
  {% if user == 'admin' %}
    <p><a href="/admin">Go to admin panel</a></p>
  {% endif %}
{% else %}
  <form method="post" action="/login">
    <input name="user" placeholder="username">
    <input name="password" placeholder="password" type="password">
    <button>Login</button>
  </form>
{% endif %}
"""

@app.route("/")
def index():
    return render_template_string(PAGE, user=session.get("user"))

@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("user")
    pw = request.form.get("password")
    if user in USERS and USERS[user] == pw:
        session["user"] = user
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

# ⚠️ Intentionally broken access control (no ownership check)
@app.route("/profile")
def profile():
    user = request.args.get("user")
    if user not in DATA:
        abort(404)
    # Missing check: should ensure session['user'] == user
    note = DATA[user]["note"]
    return f"<h3>Profile of {user}</h3><p>{note}</p>"

# ⚠️ Admin endpoint (no proper privilege enforcement)
@app.route("/admin")
def admin_panel():
    if session.get("user") != "admin":
        return "Access denied — only admin can view this (FIX ME!)", 403
    return "<h3>Welcome, admin!</h3><p>Admin-only controls go here.</p>"

if __name__ == "__main__":
    app.run(debug=True)
