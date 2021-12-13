from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['fname']
        self.last_name = data['lname']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojos_id) VALUES (%(fname)s, %(lname)s, %(age)s, NOW(), NOW(), %(dojos_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)