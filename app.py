from flask import Flask, render_template
from flask import url_for, send_from_directory

app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    """
    Returns website's home page
    """
    return render_template('home.html')

@app.route("/<path:file_path>")
def send_file(file_path):
    """
    Recommended proper way to expose static files from a directory
    """
    return send_from_directory(app.static_folder, file_path, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)