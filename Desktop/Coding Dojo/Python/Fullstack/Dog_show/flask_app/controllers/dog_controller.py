from flask_app import app
from flask import render_template, redirect, session, request, flash

#=============================================
#Create Dog Route
#=============================================
@app.route("/new_dog")
def new_dog():
    if "user_id" not in session:
        flash("Please login or register before entering site!")
        return redirect("/")
    return render_template("new_dog.html")

@app.route("/create_dog", methods = ["POST"])
def create_dog():

    #1 - validate form data
    def create_dog():
        data={
        "name": request.form["name"],
        "breed": request.form["breed"],
        "age": request.form["age"],
        "owner_id": session["owner_id"]
    }

    #2 - save new dog to database

    #3 - redirect to the dashboard




