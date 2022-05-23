from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import faction

class Friend:
    db = "friendship_schema"
    def __init__(self, data):
        self.id = data["id"]

        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.occupation = data["occupation"]
        self.age = data["age"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.faction = {} # placeholder for 1 faction

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        # Create an empty list to append our instances of friends
        all_friends = []
        # Iterate over the db results and create instances of friends with cls.
        for dict in results:
            all_friends.append( cls(dict) )
        return all_friends
    
    @classmethod
    def get_one_friend(cls, data):
        query = "SELECT * FROM friends WHERE id = %(friend_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def create_new_friend(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, age, created_at, updated_at, faction_id) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, %(age)s, NOW(), NOW(), %(faction_id)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_friend_with_faction(cls, data):
        query = """SELECT * FROM friends
                JOIN factions ON friends.faction_id = factions.id
                WHERE friends.id = %(friend_id)s;"""
        
        results = connectToMySQL(cls.db).query_db(query, data)

        # step 1) create an instance of your primary info
        # because we did SELECT * FROM friends, "friend" is the primary info, hence why we are in the friend.py
        friend = cls(results[0]) # create instance of friend

        # step 2) collect the data from the JOINED table
        # we joined onto factions, to that is our secondary info that we need to collect
        # ** MAKE SURE that you collect all of the data needed to make an instance!! **
        faction_data = {
            "id" : results[0]["factions.id"],
            "name" : results[0]["name"],
            "level" : results[0]["level"],
            "date_created" : results[0]["date_created"],
            "created_at" : results[0]["factions.created_at"],
            "updated_at" : results[0]["factions.updated_at"]
        }

        # step 3) take that collected data and pass it into the related model's class to create an instance.
        faction_instance = faction.Faction(faction_data)

        # step 4) replace the placeholder with the attached instance
        friend.faction = faction_instance

        # step 5) return the friend instance which now includes the associated instance inside of it
        return friend