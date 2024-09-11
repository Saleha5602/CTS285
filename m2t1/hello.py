# minimal Flask app
from flask import Flask # type: ignore

app = Flask(__name__)

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