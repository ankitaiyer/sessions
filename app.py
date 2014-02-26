from flask import Flask, render_template, request, redirect, session, url_for, flash
import model

app = Flask(__name__)
app.secret_key = "shhhhthisisasecret"

@app.route("/")
def index():
    if session.get("user_id"):
        return "User %s is logged in!"%session['user_id']
    else:
        return render_template("index.html")

@app.route("/", methods=["POST"])
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")

    user_id = model.authenticate(username, hash(password))
 #   return user_id
    if user_id != None:
        flash("User authenticated!")
        #session['username'] = username
        session['user_id'] = user_id
    else:
        flash("Password incorrect, there may be a ferret stampede in progress.")

    return redirect(url_for("index"))
#    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/clear_session")
def session_clear():
#    session.clear(session["hackbright"])
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
