from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import sighting

class Sighting:
    db_name = "sas_sight_sch"
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.date = data['date']
        self.num_sightings = data['num_sightings']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = []
        self.user_s = []

    @staticmethod
    def validate_sighting(sighting):
        is_valid = True
        if len(sighting['location']) < 1:
            flash("Please provide a location.")
            is_valid = False
        if len(sighting['description']) < 1:
            flash("Please provide a description.")
            is_valid = False
        if len(sighting['num_sightings']) < 1:
            flash("Please provide number of sightings.")
            is_valid = False
        if sighting['date'] == None:
            flash("Please provide the date sighted.")
            is_valid = False
        return is_valid

    @classmethod
    def save_sighting(cls, data):
        query = "INSERT INTO sightings (location, description, date, num_sightings, created_at, updated_at, user_id) VALUES (%(location)s, %(description)s, %(date)s, %(num_sightings)s, NOW(), NOW(), %(user_id)s);"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_sighting(cls, data):
        query = "SELECT * FROM sightings WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def update_sighting(cls, data):
        query = "UPDATE sightings SET location=%(location)s, description=%(description)s, date=%(date)s, num_sightings=%(num_sightings)s, updated_at=NOW() WHERE id = %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results

    @classmethod
    def delete_sighting(cls, data):
        query = "DELETE FROM sightings WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def user_sighting(cls, data):
        query = "SELECT * FROM sightings LEFT JOIN users ON sightings.user_id = users.id;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # print(results)
        all_sightings = []
        for db_row in results:
            sighting_data = {
                'id': db_row['id'],
                'location': db_row['location'],
                'description': db_row['description'],
                'date': db_row['date'],
                'num_sightings': db_row['num_sightings'],
                'created_at': db_row['created_at'],
                'updated_at': db_row['updated_at']
            }
            one_sighting = cls(sighting_data)
            user_data = {
                'id': db_row['users.id'],
                'first_name': db_row['first_name'],
                'last_name': db_row['last_name'],
                'email': db_row['email'],
                'password': db_row['password'],
                'created_at': db_row['users.created_at'],
                'updated_at': db_row['users.updated_at']
            }
            one_user = user.Users(user_data)
            one_sighting.creator = one_user
            all_sightings.append(one_sighting)
            print(all_sightings)
        return all_sightings

    @classmethod
    def get_user_for_sighting(cls, data):
        query = 'SELECT * FROM sightings LEFT JOIN users ON sightings.user_id = users.id WHERE sightings.user_id = %(user_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if not results:
            return False
        return results

    @classmethod
    def reporter(cls, data):
        query = 'SELECT * FROM sightings LEFT JOIN users ON sightings.user_id = users.id WHERE sightings.id = %(id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if not results:
            return False
        return results
