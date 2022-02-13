from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# About Page Route
@app.route("/about")
def index():
    return render_template("index.html")

# Demo Input Route
@app.route("/demo-output")
def index():
    return render_template("demo-output.html")

# Demo Output Route
@app.route("/demo-input")
def index():
    return render_template("demo-input.html")

