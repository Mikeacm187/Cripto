# lab1_traversal/app_secure.py
from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

BASE_DIR = os.path.join(os.path.dirname(__file__), "files")
os.makedirs(BASE_DIR, exist_ok=True)

# Create a sample file for students to read
sample_path = os.path.join(BASE_DIR, "report.txt")
if not os.path.exists(sample_path):
    with open(sample_path, "w") as f:
        f.write("This is a public report file.\n")

# Allowlist of served filenames
ALLOWLIST = {"report.txt"}

@app.route("/")
def index():
    return """
    <h2>Lab 1 - Directory Traversal (PATCHED)</h2>
    <p>Download endpoint enforces canonicalization and allowlist.</p>
    <p>Try: <a href="/download?name=report.txt">report.txt</a></p>
    """

def is_safe_path(base_dir, user_path):
    # canonical paths and prefix check
    base = os.path.realpath(base_dir)
    requested = os.path.realpath(os.path.join(base_dir, user_path))
    # ensure requested path is inside base directory
    return requested.startswith(base + os.sep) or requested == base

@app.route("/download")
def download():
    name = request.args.get("name")
    if not name:
        return "Missing ?name parameter", 400

    # 1) allowlist check
    if name not in ALLOWLIST:
        return "Requested file is not allowed.", 403

    # 2) canonicalization check
    if not is_safe_path(BASE_DIR, name):
        return "Invalid or unsafe path.", 400

    path = os.path.join(BASE_DIR, name)
    if not os.path.isfile(path):
        abort(404)
    return send_file(path)

if __name__ == "__main__":
    app.run(debug=True)
