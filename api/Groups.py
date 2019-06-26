from flask_restful import Resource, reqparse, request
from flask import jsonify
from dataOperations import Initialization, SQL_Operations
from db_schema import schema

class Group(Resource):
    # Grab our data layer objects
    db_resources = schema()
    sql_operations = SQL_Operations()
    
    def __init__(self):
        # Check for DB, if we cant find one, lets make one
        init = Initialization()
        return None

    # @params name - str, group name for SQL where clause
    # @return JSON dict of results found otherwise None
    def get(self, name):
        res = self.db_resources
        sql = "SELECT * FROM " + res.getGroupTableName() + " WHERE " + res.getGroupName() + " = (?);"
        # Parameterized SQL (Remember comma after parameter since we only have one parameter)
        group = self.sql_operations.valueReturningQuery(sql,(name,))   
        if(group is not None):
            return group, 200
        return "Group not found", 404

    # @params name - str, group name specifed for deletion
    # @return Boolean - true if operation succeeded, False if operation Failed
    def delete(self, name):
        sql = "DELETE FROM " + self.db_resources.getGroupTableName() + " WHERE " + self.db_resources.getGroupName() + " = (?);"
        # Parameterized SQL (Remember comma after parameter since we only have one parameter)
        deleteGroup = self.sql_operations.nonValueReturningQuery(sql,(name,))
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

    # @return JSON Dict of all results otherwise None
    def get(self):
        res = self.db_resources
        sql = "SELECT * FROM " + res.getGroupTableName()
        # Parameterized query, blank parameter because we dont have any user inputs
        allGroups = self.sql_operations.valueReturningQuery(sql,"")   
        if(allGroups is not None):
            return allGroups, 200
        return "No Results Are Available", 404

    # @return Boolean - True if operation succeeded, False if operation failed
    def post(self):
        res = self.db_resources
        parser = reqparse.RequestParser()
        parser.add_argument("group_name")
        args = parser.parse_args()
        sql = "INSERT INTO " + res.getGroupTableName() + " (" + res.getGroupName() +") VALUES (?);"
        # Parameterized SQL (Remember comma after parameter since we only have one parameter)
        insertResults = self.sql_operations.nonValueReturningQuery(sql,(args["group_name"],))
        if (insertResults):
            # JSONify our results
            succesfulResults = jsonify(inserted=True)
            succesfulResults.status_code = 201
            return succesfulResults
        badResults = jsonify(inserted=False)
        badResults.status_code = 400
        return badResults

    # @return Boolean - True if operation succeeded, False if operation failed
    def put(self):
        res = self.db_resources
        parser = reqparse.RequestParser()
        parser.add_argument("Group_ID")
        parser.add_argument("Group_Name")
        args = parser.parse_args()
        sql = "UPDATE " + res.getGroupTableName() + " SET " + res.getGroupName() +" = (?) WHERE "+ res.getGroupID() +" = (?);"
        # Parameterized SQL (Remember no comma after parameter since we have more than one parameter)
        insertResults = self.sql_operations.nonValueReturningQuery(sql,(args["Group_Name"], args["Group_ID"]))        
        if (insertResults):
            # JSONify our results
            succesfulResults = jsonify(updated=True)
            succesfulResults.status_code = 200
            return succesfulResults
        badResults = jsonify(updated=False)
        badResults.status_code = 404
        return badResults