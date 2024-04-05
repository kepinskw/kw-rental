from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='/')


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/services.html")
def services():
    return render_template("services.html")


@app.route("/rooms.html")
def rooms():
    return render_template("rooms.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")
