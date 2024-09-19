
from flask import Flask, redirect, render_template, request, url_for # type: ignore

app = Flask(__name__)
app.config["DEBUG"] = True

comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))
#old code
""" # minimal Flask app
from flask import Flask, render_template # type: ignore
#print("starting flask program", __name__)
app = Flask(__name__)
# do any app specific setup here
#for instance, loding a database
@app.route("/")
def index():
    name= " Alya Saleh"
    return render_template("main_page.html", name=name)
@app.route("/action")
def action():
    return "Hello from the action route!"

@app.route("/questions")
def questions():
    return "Tried to add another page" """