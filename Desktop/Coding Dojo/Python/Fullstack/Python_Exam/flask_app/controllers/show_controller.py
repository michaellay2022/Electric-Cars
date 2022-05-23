from flask_app import app
from flask import render_template, redirect, session, request, flash

from flask_app.models.show import Show

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
    "title": request.form["title"],
    "network": request.form["network"],
    "release_date": request.form["release_date"],
    "description": request.form["description"],
    "user_id": session["user_id"]
}

    if not Show.validate_show(data):
        return redirect("/new_show")

    #2 - save new show to database
    Show.create_show(data)


    #3 - redirect to the dashboard
    return redirect ("/dashboard")

#=============================================
#Create One Show Route
#=============================================

@app.route("/show/<int:show_id>")
def display_show(show_id):
    if "user_id" not in session:
        flash("Please login or register before entering site!")
        return redirect("/")
  
    #1 - query for show info w/ associated info of user
    data = {
        "show_id": show_id
    }
    show = Show.get_show_with_user(data)


    return render_template("display_show.html", show = show)

#=============================================
#Edit One Show Route
#=============================================

@app.route("/show/edit/<int:show_id>")
def edit_show(show_id):
    #1, query for the show we want to update
    data = {
        "show_id": show_id
    }
    show = Show.get_show_with_user(data)

    #2, pass show info to the html
    return render_template("edit_show.html", show = show)

@app.route("/show/<int:show_id>/update", methods = ["POST"])
def update_show(show_id):
    #1 - validate our form data

    data={
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"], 
        "show_id": show_id
    }

    if not Show.validate_show(data):
        return redirect(f"/show/edit/{show_id}")

    #2, udpate info
    Show.update_dog_info(data)

    #redirect
    return redirect("/dashboard")
        
        #=============================================
#Delete One Show Route
#=============================================
@app.route("/show/<int:show_id>/delete")
def delete_show(show_id):
    data = {
        "show_id": show_id
    }
    Show.delete_show(data)

    return redirect("/dashboard")
    