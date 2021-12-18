from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-z0-9.+_-]+\.[a-zA-Z]+$')

class Users:
    db_name = "login_and_registration"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.dob = data['dob']
        self.fav_language = data['fav_language']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
        if len(user['dob']) < 9:
            flash("Please provide a valid birthday.")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, dob, fav_language, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, %(dob)s, %(fav_language)s, NOW(), NOW());"
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
        return cls(results[0])
