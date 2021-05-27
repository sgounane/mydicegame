from flask import Flask, render_template, request, session

from werkzeug.utils import redirect

app=Flask(__name__)
app.config["SECRET_KEY"]="my secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    if session.get("user"):
        return render_template("game.html",user=session.get("user"))
    return redirect('/login')

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        session["user"]=request.form.get("user")
        return redirect('/game')
    elif session.get("user"):
       return  redirect('/game')
    return render_template("login.html")

app.run(debug=True, port=3333, host='0.0.0.0')