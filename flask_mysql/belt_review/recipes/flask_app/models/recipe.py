from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Recipes:
    db_name = "recipes_sch"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.thirty = data['thirty']
        self.descr = data['descr']
        self.inst = data['inst']
        self.d_made = data['d_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 1:
            flash("Must provide a name for this recipe.")
            is_valid = False
        if len(recipe['descr']) < 8:
            flash("Must provide a description longer than 8 characters.")
            is_valid = False
        if len(recipe['inst']) < 8:
            flash("Must provide instructions longer than 8 characters.")
            is_valid = False
        return is_valid

    @classmethod
    def save_recipe(cls, data):
        query = "INSERT INTO recipes (name, thirty, descr, inst, d_made, created_at, updated_at, user_id) VALUES (%(name)s, %(thirty)s, %(descr)s, %(inst)s, %(d_made)s, NOW(), NOW(), %(user_id)s);"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results

    @classmethod
    def user_recipes(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        # print(results)
        all_recipes = []
        for db_row in results:
            recipe_data = {
                'id': db_row['id'],
                'name': db_row['name'],
                'thirty': db_row['thirty'],
                'descr': db_row['descr'],
                'inst': db_row['inst'],
                'd_made': db_row['d_made'],
                'created_at': db_row['created_at'],
                'updated_at': db_row['updated_at']
            }
            one_recipe = cls(recipe_data)
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
            one_recipe.user = one_user
            all_recipes.append(one_recipe)
            print(all_recipes)
        return all_recipes

    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if not results:
            return False
        return cls(results[0])


    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name=%(name)s, thirty=%(thirty)s, descr=%(descr)s, inst=%(inst)s, d_made=%(d_made)s, updated_at=NOW() WHERE id = %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)