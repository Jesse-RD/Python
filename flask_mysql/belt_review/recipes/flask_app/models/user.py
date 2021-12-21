from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

from flask_app.models import recipe

class Users:
    db_name = "recipes_sch"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @staticmethod
    def validate_register(user):
        is_valid = True
        users_with_email = Users.get_by_email({'email': user['email']})
        print(users_with_email)
        if users_with_email:
            flash("There is already an account associated with this email.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must have more than 8 characters.")
            is_valid = False
        if (user['password']) != (user['r_password']):
            flash("Repeated passwords must match!")
            is_valid = False
        if len(user['fname']) < 2:
            flash("Please provide a first name.")
            is_valid = False
        if len(user['lname']) < 2:
            flash("Please provide a last name.")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        users_with_email = Users.get_by_email({'email': user['email']})
        if not users_with_email:
            flash("There is no record this account exists.")
            is_valid = False
        if len(user['email']) < 8:
            flash("Invalid Username/Password")
            is_valid = False
        if len(user['password']) < 8:
            flash("Invalid Username/Password")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_profile(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if not results:
            return False
        one_user = cls(results[0])
        return one_user

    @classmethod
    def profile_recipes(cls, data):
        query = 'SELECT * FROM users LEFT JOIN recipes ON recipes.user_id = users.id WHERE users.id = %(id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if not results:
            return False
        one_user = cls(results[0])
        for db_row in results:
            user_data = {
                'id': db_row['recipes.id'],
                'fname': db_row['first_name'],
                'lname': db_row['last_name'],
                'name': db_row['name'],
                'thirty': db_row['thirty'],
                'descr': db_row['descr'],
                'inst': db_row['inst'],
                'd_made': db_row['d_made'],
                'created_at': db_row['recipes.created_at'],
                'updated_at': db_row['recipes.updated_at']
            }
            one_recipe = recipe.Recipes(user_data)
            one_user.recipes.append(one_recipe)
        return one_user

