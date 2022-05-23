from flask_app import app
from flask import render_template, redirect, session, request

# import the class from friend.py
from flask_app.models.friend import Friend
from flask_app.models.faction import Faction

# ======================================================
# 'Read' All Route / Dashboard
# ======================================================

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    all_friends = Friend.get_all()

    # call additional method to grab all factions
    all_factions = Faction.get_all_factions()
    return render_template("index.html", all_friends = all_friends, all_factions = all_factions)

# ======================================================
# 'Read' One Route
# ======================================================

@app.route("/friend/<int:friend_id>")
def one_friend(friend_id):
    query_data = {
        "friend_id" : friend_id
    }
    one_friend = Friend.get_friend_with_faction(query_data)
    return render_template("show_one.html", one_friend = one_friend)

# ======================================================
# 'Create' One Routes
# ======================================================

@app.route("/friend/new")
def add_friend():
    all_factions = Faction.get_all_factions()
    return render_template("add_friend.html", all_factions = all_factions)

@app.route("/friend/create", methods=["POST"])
def create_friend():
    #1 - collect the information from our form to send to query
    query_data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "occupation" : request.form["occupation"],
        "age" : int(request.form["age"]),
        "faction_id" : request.form["faction_id"]
    }
    #2 - call on query from our model file
    new_friend_id = Friend.create_new_friend(query_data)

    #3 - redirect elsewhere once query is done
    return redirect(f"/friend/{new_friend_id}")