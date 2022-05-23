from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
# the first user will be import from flask app->models->user.py


# ===============================================
# 'READ' ALL ROUTE
# ===============================================

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

# ===============================================
# 'READ' ONE ROUTE
# ===============================================


@app.route("/user/<int:user_id>")
def one_user(user_id):  # whatever id came through, it will label as user_id
    query_data = {
        "id": user_id

    }
    one_user = User.get_one_user(query_data)
    # the first one_user is for displaying in the html
    return render_template("show_one.html", one_user=one_user)

# ===============================================
# 'CREATE' ONE ROUTES
# ===============================================


@app.route("/user/new")
def add_user():
    return render_template("add_user.html")


@app.route("/user/create", methods=["POST"])
def create_user():
    print(request.form)

    # 1 - collect information from our form to send to query
    query_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "occupation": request.form["occupation"],
    }
    # 2 - call on query from our model file
    # when run an INSERT query, you will get an ID.
    new_user_id = User.create_new_user(query_data)

    # 3 - redirect elsewhere once query is done

    return redirect("/")

# ==================================================
# Edit a user
# ==================================================

# this one for rendering the page


@app.route("/user/update/<int:id>", methods=["POST"])
def update_user(id):
    print(request.form)

    # 1 - collect information from our form to send to query
    query_data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "occupation": request.form["occupation"],
    }
    # 2 - call on query from our model file
    # new_user_id = User.edit_new_user(query_data)
    # no need to include new_user_id since we are not create a new user
    User.edit_new_user(query_data)

    # 3 - redirect elsewhere once query is done

    return redirect("/users")


@app.route("/user/edit/<int:id>")
def edit_user(id):
    # data is a new variable
    data = {"id": id
            # "id" is the key in the dict
            }
    user = User.get_one_user(data)  # right side from the model
    return render_template("edit_user.html", user=user)


@app.route("/user/destroy/<int:id>")
def destroy(id):
    data = {
        "id": id
    }
    User.destroy(data)
    return redirect('/users')
