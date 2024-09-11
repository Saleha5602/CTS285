# minimal Flask app
from flask import Flask, render_template # type: ignore
#print("starting flask program", __name__)
app = Flask(__name__)
# do any app specific setup here
#for instance, loding a database
@app.route("/")
def index():
    name= "Alya"
    return render_template("main_page.html", name=name)
@app.route("/action")
def action():
    return "Hello from the action route!"