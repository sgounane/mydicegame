from flask import Flask, render_template, request
from werkzeug.utils import redirect

app=Flask(__name__)

global user
user=""
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    global user
    if(len(user)>0):
        return render_template("game.html",user=user)
    return redirect('/login')

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        global user
        user=request.form.get("user")
        return redirect('/game')
    elif len(user)>0:
       return  redirect('/game')
    return render_template("login.html")

app.run(debug=True, port=3333, host='0.0.0.0')