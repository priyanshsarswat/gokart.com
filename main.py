from flask import Flask
import random
from flask.templating import render_template
app = Flask(__name__)
@app.route("/")
def templating():
    return render_template("index.html")
@app.route("/action")
def act():
    return"This is a web-page designed by me By python and html(Hyper-text markup language) <marquee><button>Click here</button></marquee>"
@app.route("/home")
def home():
    return render_template("img.html")
@app.route("/anotheraction")
def another_action():
    return"<b><button onclick=window.location.href='/contact'>Click here to contact</button></b>"
@app.route("/contact")
def contact():
    return"<b><marquee>This is contact page call on:9424772802</marquee></b>"

@app.route("/else")
def else2():
    return"this is else page click here to roll<button onclick=window.location.href='/dice'>Roll</button>"
@app.route("/dice")
def roll():
    return(random.choice('\u2680''\u2681''\u2682''\u2683''\u2684''\u2685'))
if __name__ == "__main__":
    app.run(debug=True)