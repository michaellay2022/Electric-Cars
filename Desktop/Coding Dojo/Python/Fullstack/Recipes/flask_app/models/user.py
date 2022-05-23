from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

bcrypt = Bcrypt(app)

class User: 
    db = "recipe_schema"

    def __init__(self, data):
        self.id = data['id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_register(form_data):
        is_valid = True

        if len(form_data['first_name']) <2:
            flash("First name must be at least 2 characters")
            is_valid = False
            
        if len(form_data['last_name']) <2:
            flash("Last name must be at least 2 characters")
            is_valid = False

        if len(form_data["password"]) < 3:
            flash("Password must be at least 3 characters long!")
            is_valid = False

        if (form_data["password"]) != form_data["password_confirmation"]:
            flash("Password and Password Confirmation must match! ")
            is_valid = False

        if not EMAIL_REGEX.match(form_data["email"]):
            flash("Please enter a valid email address!")
            is_valid = False

        return is_valid

    @classmethod
    def register_user(cls, data):
        