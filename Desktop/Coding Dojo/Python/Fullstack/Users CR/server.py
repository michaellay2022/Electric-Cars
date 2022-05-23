from flask import Flask, render_template, redirect, request, session
from user import User
# this will import the user class from users.py
app = Flask(__name__)

app.secret_key = "adopfjadjf'j"

#===============================================
# 'READ' ALL ROUTE
#===============================================

@app.route("/")
def index():
    return redirect("./users")


@app.route('/users')
def users():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    # use OOP to get all the stuffs and send us actual objects
    return render_template("users.html", all_users=users)
    # the all_users will display on the users.html inside the {% %}

#===============================================
# 'READ' ONE ROUTE
#===============================================


@app.route("/user/<int:user_id>")
def one_user(user_id):  # whatever id came through, it will label as user_id
    query_data = {
        "id": user_id

    }
    one_user = User.get_one_user(query_data)
    # the first one_user is for displaying in the html
    return render_template("show_one.html", one_user=one_user)

#===============================================
#'CREATE' ONE ROUTES
#===============================================

@app.route("/user/new")
def add_user():
    return render_template("add_user.html")


@app.route("/user/create", methods=["POST"])
def create_user():
    print(request.form)
    
    #1 - collect information from our form to send to query
    query_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "occupation": request.form["occupation"],
    }
    #2 - call on query from our model file
    #when run an INSERT query, you will get an ID.
    new_user_id = User.create_new_user(query_data)

    #3 - redirect elsewhere once query is done

    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)
