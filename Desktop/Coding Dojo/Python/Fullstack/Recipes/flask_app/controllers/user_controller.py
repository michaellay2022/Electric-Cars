from flask_app import app
from flask import render_template, redirect, session, request, flash

from flask_bcrypt import flask_bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.user import User


@app.route("/")
def index():
    return render_template("index.html")

#=====================================
#REGISTER ROUTE
#=====================================
@app.route("/register", methods=["POST"])
def register_user():

    # 1 -- validate user
    if not User.validate_register(request.form):
        return redirect("/")

    # 2 aside, convert password by bcrypt
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # 2 - collect data from form
    query_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash,
    }

    #Call the save @classmethod on User
    #where you run query to database (INSERT) or you can say call on query from our model file
    user_id = User.register_user





