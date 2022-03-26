from flask import Flask, render_template, request
from twint_integrate.twint_search import search
from twint_wordcloud.wordcloud_html import word_cloud, row_count
from predict_tweets.model import twint_parse
from predict_tweets.predictedData import predictedTweets


app = Flask(__name__, template_folder="templates", static_folder='static')

title = "BCC ML"
subtitle = "BERT Catches COVID using Machine Learning"
footer = "This Single Page Application is powered by Flask and JQuery"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.getlist("user_handle")
        csv = search(data[0])

        # write file named userTweets
        f = open("userTweets.csv", "w")
        f.write(csv)
        f.close()

    return render_template("index.html", title=title, footer=footer)

@app.route("/about")
def about():
    return render_template("index.html", title=title, subtitle=subtitle, footer=footer)

# Demo Input Route
@app.route("/demo-input")
def demo_input():
    return render_template("demo-input.html", title=title, subtitle=subtitle, footer=footer)

# Demo Output Route
@app.route("/demo-output")
def demo_output():
    rowcount = row_count("userTweets.csv")
    wc = word_cloud("predictedTweets.csv")
    twint_parse('userTweets.csv')
    predict, df = predictedTweets("predictedTweets.csv")
    return render_template("demo-output.html", title=title, subtitle=subtitle, footer=footer, wc=wc, tweets=rowcount, misinfo=predict["misinfo"], handle=predict["handle"], html=df.to_html(index=False, classes=["data", "mystyle"]))  

if __name__ == '__main__':
    app.run(debug=True)
