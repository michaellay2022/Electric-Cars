from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import dojo

class Ninja:
    def __init__(self, data):
        self.id = data["id"]

        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.dojo = {}; #this will be a single instance that go into that field

    @classmethod
    def create_ninja(cls, data):
        # query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s,(%(last_name)s,(%(age)s, NOW(), NOW())"
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s)"

        results = connectToMySQL('dojos_and_ninjas_schema'). query_db(query, data)
        return results

    @classmethod
    def get_ninjas_with_dojos():
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON dojo_id = dojos.id;"
        results = connectToMySQL('dojos_and_ninjas_schema'). query_db(query)
        
        ninja = []

        for row in results:
            ninja = cls(row)

            dojo_data = {
                "id": row ["id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["dojo.created_at"],
                "updated_at": row["dojoupdated_at"],
            }
            ninja.dojo = dojo.Dojo(dojo_data)

            ninjas.append(ninja)

        return ninja
