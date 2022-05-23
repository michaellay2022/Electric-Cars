from flask_app import app
from flask import render_template, redirect, session, request, flash

#=============================================
#Create Show Route
#=============================================
@app.route("/new_show")
def new_show():
    if "user_id" not in session:
        flash("Please login or register before entering site!")
        return redirect("/")
    return render_template("new_show.html")

@app.route("/create_show", methods = ["POST"])


    #1 - validate form data
def create_show():
    data={
    "title": request.form["name"],
    "network": request.form["network"],
    "release_date": request.form["release_date"],
    "description": request.form["description"],
    "user_id": session["user_id"]
}

    #2 - save new show to database

    #3 - redirect to the dashboard




