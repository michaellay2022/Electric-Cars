from flask_app.config.mysqlconnection import connectToMySQL


class User:
    db = "userscr_schema"  # declare your schema name here **********

    def __init__(self, data):
        self.id = data['id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.occupation = data['occupation']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database, and put them into instances of our class
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users_cr;"  # users_cr is the table name
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of users
        user_instances = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:  # why the instructor call dict in results?
            user_instances.append(cls(user))
        return user_instances

    @classmethod
    def get_one_user(cls, data):
        # make sure the %(id)s match the id list on the app route one_user "id": user_id
        query = "SELECT * FROM users_cr WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def create_new_user(cls, data):  # create_new_user is from the server.py===#

        # the INSERT INTO users_cr is the table name
        query = "INSERT INTO users_cr (first_name, last_name, occupation, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, %(email)s,NOW(), NOW());"
        # this query is associated with the query_data in the server.py where query_data = {}
        results = connectToMySQL(cls.db).query_db(query, data)
        return results  # when return results, it is going to be an ID because of INSERT QUERY

    @classmethod
    def edit_new_user(cls, data):  # edit a user

        # use the Update function on mysql
        query = "UPDATE users_cr SET first_name = %(first_name)s, last_name= %(last_name)s, email=%(email)s,occupation =%(occupation)s WHERE id = %(id)s"   
        return connectToMySQL(cls.db).query_db(query, data)
        
    @classmethod
    def destroy(cls,data):
        query="DELETE FROM users_cr WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
