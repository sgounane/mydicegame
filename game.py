from flask import Flask, render_template, request
from werkzeug.utils import redirect

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        return redirect('/game')
    return render_template("login.html")

app.run(debug=True, port=3333, host='0.0.0.0')