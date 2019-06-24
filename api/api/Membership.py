from flask_restful import Resource
from dataOperations import Initialization, SQL_Operations
from db_schema import schema

class Membership(Resource):
    db_resources = schema()
    sql_operations = SQL_Operations()
    
    def __init__(self):
        # Check for DB, if we cant find one, lets make one
        init = Initialization()
        return None
    # @params :id = int, membership id for the where clause
    # @return = JSON dict of the user found, otherwise None
    def get(self, id):
        res = self.db_resources
        sql = "SELECT * FROM " + res.getMembershipTableName() + " WHERE " + res.getMembershipID() + " = (?);"
        mem = self.sql_operations.valueReturningQuery(sql,(id,))   
        if(mem is not None):
            return mem, 200
        return "Membership not found", 404

    def post(self, name):
        # ======= Method Stub Assignment Doesn't Require Operation
        return user, 400

    def put(self, name):
        # ======= Method Stub Assignment Doesn't Require Operation
        return user, 400

    def delete(self, name):
        # ======= Method Stub Assignment Doesn't Require Operation
        return user, 400

class Memberships(Resource):
    db_resources = schema()
    sql_operations = SQL_Operations()

    def __init__(self):
       # Check for DB, if we cant find one, lets make one
        init = Initialization()
        return None
    # @return JSON dict of all memberships, otherwise None
    def get(self):
        res = self.db_resources
        sql = "SELECT * FROM " + res.getMembershipTableName()
        mems = self.sql_operations.valueReturningQuery(sql, "")   
        if(mems is not None):
            return mems
        return "No Results Are Available", 404
