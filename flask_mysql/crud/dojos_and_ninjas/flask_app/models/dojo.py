from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojos:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for one_dojo in results:
            dojos.append(cls(one_dojo))
        return dojos

    @classmethod
    def save_dojo(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(dname)s, NOW(), NOW());'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def dojo_with_ninjas(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        one_dojo = cls(results[0])
        for db_row in results:
            ninja_data = {
                'id': db_row['ninjas.id'],
                'fname': db_row['first_name'],
                'lname': db_row['last_name'],
                'age': db_row['age'],
                'created_at': db_row['ninjas.created_at'],
                'updated_at': db_row['ninjas.updated_at']
            }
            one_ninja = ninja.Ninja(ninja_data)
            one_dojo.ninjas.append(one_ninja)
        return one_dojo