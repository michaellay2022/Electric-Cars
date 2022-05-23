from flask_app import app
from flask import render_template, redirect, session, request



from flask_app.models.dojo import Dojo #import this one first, the reason being that we will run a query to get_all_dojo
#                        
from flask_app.models.ninja import Ninja

#==================================
#Main Page / Dashboard
#======================================
@app.route("/dojos")
def dojos():
    #this will be a join query
    #Ninja.get_ninjas_with_dojos()
    # all_ninjas = Ninja.get_ninjas_with_dojos()
    # return render_template("dojos.html", all_ninjas = all_ninjas)
    return render_template("dojos.html", all_dojos = Dojo.get_all_dojos())


#==================================
#Create Ninja Routes
#======================================
@app.route("/ninja/new")
def new_ninja():
    dojos = Dojo.get_all_dojos()

    return render_template("new_ninja.html", dojos = dojos)

@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    data={
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }

    # Ninja.create_ninja(data)
    Ninja.create_ninja(data)

    return redirect("/dojos")