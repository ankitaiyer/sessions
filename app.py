from flask import Flask, render_template, request, redirect, session, url_for, flash
import model
from urlparse import urlparse

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

@app.route("/user/<username>")
def show_user_profile(username):
    rows = model.get_all_posts(username)
    return render_template("wall.html", rows=rows, username=username)

@app.route("/user/<username>", methods=["POST"])
def post_to_wall(username):
    print "****************************************"
    # print "USERNAME", username
    owner_id = model.get_user_by_name(username)
    print "OWNER_ID", owner_id
    author_id = session.get("user_id")
    wall_post = request.form.get("wall_post")
    print "AUTHOR ID", author_id
    print "WALL POST", wall_post
    model.submit_post(owner_id,author_id,wall_post)
    return redirect(url_for("show_user_profile", username=username))

if __name__ == "__main__":
    app.run(debug = True)
