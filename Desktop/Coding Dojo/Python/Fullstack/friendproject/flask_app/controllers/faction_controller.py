from flask_app import app
from flask import render_template, redirect, session, request

# import the class from friend.py
from flask_app.models.friend import Friend
                    #.friend is the friend.py
from flask_app.models.faction import Faction 
                        #this is a class Faction

# ======================================================
# 'Create' One Routes
# ======================================================

#step 1, have a route for render
@app.route("/faction/new")
def new_faction():
    return render_template("add_faction.html")

#step 2, have a route for processing 
@app.route("/faction/create", methods = ["POST"])
def create_faction():

    #1, collect the information from our form to send to query
    query_data = {
        "name" : request.form["name"],
        "level" : request.form["level"],
        "date_created" : request.form["date_created"]
    }
    #when create/INSERT something to Database, it will return ID that why we call it as new_faction_id
                        #this created_new_faction is created first before call it in the classmethod.(query_data) is here so we can pass info here.
    new_faction_id = Faction.created_new_faction(query_data)
                    #Faction here is just a Faction class name
    return redirect("/")

# ======================================================
# 'Show' One Route
# ======================================================

@app.route("/faction/<int:faction_id>")
def show_one_faction(faction_id):
    query_data = {
        "faction_id" : faction_id
    }

    one_faction = Faction.get_faction_with_friends(query_data)
    return render_template("show_one_faction.html", one_faction = one_faction)