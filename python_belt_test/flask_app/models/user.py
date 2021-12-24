from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

from flask_app.models import sighting

class Users:
    db_name = "sas_sight_sch"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sightings = []

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
        if len(user['first_name']) < 2:
            flash("Please provide a first name.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Please provide a last name.")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        users_with_email = Users.get_by_email({'email': user['email']})
        if not users_with_email:
            flash("Something went wrong.")
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
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_profile(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if not results:
            return False
        one_user = cls(results[0])
        return one_user

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def user_for_sighting(cls, data):
        query = 'SELECT * FROM users LEFT JOIN sightings ON sightings.user_id = users.id WHERE users.id = %(id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if not results:
            return False
        one_user = cls(results[0])
        for db_row in results:
            user_data = {
                'id': db_row['sightings.id'],
                'first_name': db_row['first_name'],
                'last_name': db_row['last_name'],
                'location': db_row['location'],
                'description': db_row['description'],
                'date': db_row['date'],
                'num_sightings': db_row['num_sightings'],
                'created_at': db_row['sightings.created_at'],
                'updated_at': db_row['sightings.updated_at']
            }
            one_sighting = sighting.Sighting(user_data)
            one_user.sightings.append(one_sighting)
        return one_user
