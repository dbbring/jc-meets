from flask_restful import Resource
from dataOperations import Initialization, SQL_Operations
from db_schema import schema

class Role(Resource):
    # Grab our data layer objects
    db_resources = schema()
    sql_operations = SQL_Operations()
    
    def __init__(self):
        # Check for DB, if we cant find one, lets make one
        init = Initialization()
        return None

    # @params :name = str, role name for where clause
    # @return = JSON dict of the user found, otherwise None
    def get(self, name):
        res = self.db_resources
        sql = "SELECT * FROM " + res.getRoleTableName() + " WHERE " + res.getRoleName() + " = (?);"
        role = self.sql_operations.valueReturningQuery(sql,(name,))   
        if(role is not None):
            return role, 200
        return "Role not found", 404

    def post(self, name):
        # ======= Method Stub Assignment Doesn't Require Operation
        return user, 400

    def put(self, name):
        # ======= Method Stub Assignment Doesn't Require Operation
        return user, 400

    def delete(self, name):
        # ======= Method Stub Assignment Doesn't Require Operation
        return user, 400

class Roles(Resource):
    # Grab our data layer objects
    db_resources = schema()
    sql_operations = SQL_Operations()

    def __init__(self):
       # Check for DB, if we cant find one, lets make one
        init = Initialization()
        return None

    # @return JSON dict of all roles, otherwise None
    def get(self):
        res = self.db_resources
        sql = "SELECT * FROM " + res.getRoleTableName()
        roles = self.sql_operations.valueReturningQuery(sql, "")   
        if(roles is not None):
            return roles
        return "No Roles Are Available", 404