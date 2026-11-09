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

@app.route("/")
def index():
    return """
    <h2>Lab 1 – Directory Traversal</h2>
    <p>Try to download files: <a href="/download?name=report.txt">report.txt</a></p>
    <p>Download endpoint: <code>/download?name=&lt;filename&gt;</code></p>
    """

# ⚠️ Intentionally vulnerable endpoint
@app.route("/download")
def download():
    name = request.args.get("name")
    if not name:
        return "Missing ?name parameter", 400
    file_path = os.path.join(BASE_DIR, name)
    try:
        return send_file(file_path)
    except FileNotFoundError:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
