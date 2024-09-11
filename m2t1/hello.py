# minimal Flask app
from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>Hello World</h1>
    <h3>--------------------------</h3> 
    <p>Name: Alya Saleh</p> 
    <p>Class: CTS285</p>"""