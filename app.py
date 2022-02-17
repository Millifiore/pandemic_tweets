from flask import Flask, render_template, request
from twint_integrate.twint_search import search

app = Flask(__name__, template_folder="templates", static_folder='static')

title = "detecting COVID-19 misinformation in text-based social media posts."
footer = "This Single Page Application is powered by Flask and JQuery"

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        data = request.form.getlist("user_handle")
        search(data[0])
    return render_template("index.html", title=title, footer=footer)

# Demo Input Route
@app.route("/demo-input")
def demo():
    return render_template("demo-input.html", title=title, footer=footer)

# Demo Output Route
@app.route("/demo-output")
def input():
    return render_template("demo-output.html", title=title, footer=footer)

if __name__ == '__main__':
    app.run(debug=True)
