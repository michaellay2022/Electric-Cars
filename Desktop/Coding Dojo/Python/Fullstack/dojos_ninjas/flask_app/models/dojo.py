from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import dojo

class Dojo:
    def __init__(self, data):
        # db = "dojos_and_ninjas_schema"

        self.id = data["id"]

        self.name = data["name"]
      
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        # self.friends = [] # placeholder/empty list for multiple friends
        # self.dojo = {};

    @classmethod
    def create_dojo(cls, data):

        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());" #this line is only to define query

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return results
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []

        for one_dojo in results:
            dojos.append(cls(one_dojo))

        return dojos
    