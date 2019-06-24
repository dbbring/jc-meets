from flask_restful import Resource, reqparse
from flask import jsonify
from dataOperations import Initialization, SQL_Operations
from db_schema import schema
import sys

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
        group = self.sql_operations.valueReturningQuery(sql)   
        if(group is not None):
            return group, 200
        return "Group not found", 404

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
        allGroups = self.sql_operations.valueReturningQuery(sql)   
        if(allGroups is not None):
            return allGroups, 200
        return "No Results Are Available", 404

    
    def post(self):
        res = self.db_resources
        parser = reqparse.RequestParser()
        parser.add_argument("group_name")
        args = parser.parse_args()
        sql = "INSERT INTO " + res.getGroupTableName() + " (" + res.getGroupName() +") VALUES ('"+args["group_name"]+"');"
        insertResults = self.sql_operations.nonValueReturningQuery(sql)
        if (insertResults):
            succesfulResults = jsonify(inserted=True)
            succesfulResults.status_code = 201
            return succesfulResults
        badResults = jsonify(inserted=False)
        badResults.status_code = 400
        return badResults

    def put(self):
        res = self.db_resources
        parser = reqparse.RequestParser()
        parser.add_argument("group_id")
        parser.add_argument("group_name")
        args = parser.parse_args()
        sql = "UPDATE " + res.getGroupTableName() + " SET " + res.getGroupName() +" = '"+args["group_name"]+"' WHERE "+ res.getGroupID() +" = " + args["group_id"] + ";"
        insertResults = self.sql_operations.nonValueReturningQuery(sql)
        if (insertResults):
            succesfulResults = jsonify(inserted=True)
            succesfulResults.status_code = 200
            return succesfulResults
        badResults = jsonify(inserted=False)
        badResults.status_code = 404
        return badResults