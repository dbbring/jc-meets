from flask_restful import Resource
from dataOperations import Initialization, SQL_Operations
from db_schema import schema

class User(Resource):
    # Grab our data layer objects
    db_resources = schema()
    sql_operations = SQL_Operations()
    
    def __init__(self):
        # Check for DB, if we cant find one, lets make one
        init = Initialization()
        return None

    # @params :name = str, user first name for where clause
    # @return = JSON dict of the user found, otherwise None
    def get(self, name):
        res = self.db_resources
        sql = "SELECT * FROM " + res.getUserTableName() + " WHERE " + res.getUserFirstName() + " = (?);"
        # Use parameterized query for finding a specific user
        user = self.sql_operations.valueReturningQuery(sql,(name,))   
        if(user is not None):
            return user, 200
        return "User not found", 404

    def post(self, name):
        # ======= Method Stub Assignment Doesn't Require Operation
        return user, 400

    def put(self, name):
        # ======= Method Stub Assignment Doesn't Require Operation
        return user, 400

    def delete(self, name):
        # ======= Method Stub Assignment Doesn't Require Operation
        return user, 400

class Users(Resource):
    # Grab our data layer objects
    db_resources = schema()
    sql_operations = SQL_Operations()

    def __init__(self):
       # Check for DB, if we cant find one, lets make one
        init = Initialization()
        return None

    # @return JSON dict of all users, otherwise None
    def get(self):
        res = self.db_resources
        sql = "SELECT * FROM " + res.getUserTableName()
        user = self.sql_operations.valueReturningQuery(sql,"")   
        if(user is not None):
            return user
        return "No Results Are Available", 404