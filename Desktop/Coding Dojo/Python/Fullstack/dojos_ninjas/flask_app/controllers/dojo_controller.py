from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.dojo import Dojo
# from flask_app.models.ninja import Ninja

#==================================
#Create Dojo Route
#======================================

@app.route("/new_dojo", methods=["POST"])
def new_dojo():
    data={
        #"name" line up with the model and database
        #"dojo_html_name" line up with my dojos.html
        "name":request.form["dojo_html_name"]
    }


    #then run a query, run through an dojo model

    Dojo.create_dojo(data)
    return redirect("/dojos")

@app.route("/show_one_dojo/<int:id>")
def show_dojo(id):
    data = {
        "id":id
    }
    # return render_template("show_dojo.html", dojo = Dojo.get_ninjas_with_dojos(data))
    return render_template("show_dojo.html")