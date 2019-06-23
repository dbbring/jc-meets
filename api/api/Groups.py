from flask_restful import Resource, reqparse
from flask import jsonify
from dataOperations import Initialization, SQL_Operations
from db_schema import schema

class Group(Resource):
    db_resources = schema()
    sql_operations = SQL_Operations()
    
    def __init__(self):
        # Check for DB, if we cant find one, lets make one
        init = Initialization()
        return None

    def get(self, name):
        res = self.db_resources
        sql = "SELECT * FROM " + res.getGroupTableName() + " WHERE " + res.getGroupName() + " = '" + name + "';"
        user = self.sql_operations.valueReturningQuery(sql)   
        if(user is not None):
            return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in self.users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        self.users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in self.users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        self.users.append(user)
        return user, 201

    def delete(self, name):
        sql = "DELETE FROM " + self.db_resources.getGroupTableName() + " WHERE " + self.db_resources.getGroupName() + " = '" + name + "';"
        deleteGroup = self.sql_operations.nonValueReturningQuery(sql)
        if (deleteGroup):
            succesfulResults = jsonify(deleted=True)
            succesfulResults.status_code = 200
            return succesfulResults
        notFoundResults = jsonify(deleted=False)
        notFoundResults.status_code = 404
        return notFoundResults

class Groups(Resource):
    db_resources = schema()
    sql_operations = SQL_Operations()

    def __init__(self):
       # Check for DB, if we cant find one, lets make one
        init = Initialization()
        return None

    def get(self):
        res = self.db_resources
        sql = "SELECT * FROM " + res.getGroupTableName()
        user = self.sql_operations.valueReturningQuery(sql)   
        if(user is not None):
            #results = jsonify(user)
            #results.status_code = 200
            return user
        return "No Results Are Available", 404