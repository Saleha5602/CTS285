# minimal Flask app
from flask import Flask # type: ignore
#print("starting flask program", __name__)
app = Flask(__name__)
# do any app specific setup here
#for instance, loding a database
@app.route("/")
def index():
    return """<h1>Hello World</h1>
    <h3>--------------------------</h3> 
    <p>Name: Alya Saleh</p> 
    <p>Class: CTS285</p>
    <a href="action">Click here</a>
    """
@app.route("/action")
def action():
    return "Hello from the action route!"