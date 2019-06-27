from flask_restful import Resource, reqparse, request
from flask import jsonify, Request
import json
from dataOperations import Initialization, SQL_Operations
from db_schema import schema
from Groups import Group
from Users import User
import sys

class Upload(Resource):
    # Grab our data layer objects
    db_resources = schema()
    sql_operations = SQL_Operations()
    
    def __init__(self):
        # Check for DB, if we cant find one, lets make one
        init = Initialization()
        return None

    # @return ERR Request not allowed
    def get(self, name):
        # Method Stub Upload is POST only
        return "GET Requests are not allowed on this enpoint.", 400

    # @return Boolean - True if operation succeeded, False if operation failed
    def post(self):
        res = self.db_resources
        source = request.get_json()
        badReq = False
        groupInserted = False
        userInserted = False

        for x in source:
            # Check to see the group already exisits because SQLite will just make more fields reguardless of same content
            groupInDB = self.sql_operations.ifExistsQuery(res.getGroupTableName(), res.getGroupName(), x["Group_Name"])
            # Check if user already exists
            userFirstNameInDB = self.sql_operations.ifExistsQuery(res.getUserTableName(), res.getUserFirstName(), x["First_Name"])
            userLastNameInDB = self.sql_operations.ifExistsQuery(res.getUserTableName(), res.getUserLastName(), x["Last_Name"])
            if(groupInDB):
                # Group Already Exists, Stub here incase we want to perform some action in the future
                pass
            else:
                groupSql = "INSERT INTO " + res.getGroupTableName() + " (" + res.getGroupName() +") VALUES (?);"
                # Parameterized SQL (Remember comma after parameter since we only have one parameter)
                self.sql_operations.nonValueReturningQuery(groupSql,(x["Group_Name"],))   
                groupInserted = True
            if(userFirstNameInDB and userLastNameInDB):
                pass
            else:
                userSql = "INSERT INTO " + res.getUserTableName() + " (" + res.getUserFirstName() + "," + res.getUserLastName() +") VALUES (?,?);"
                self.sql_operations.nonValueReturningQuery(userSql,(x["First_Name"],x["Last_Name"]))    
                userInserted = True
            # get user id and group id
            grp = Group.get(self,x["Group_Name"])
            grpID = grp[0][0]["Group_ID"]
            usr = User.get(self,x["First_Name"])
            usrID = usr[0][0]["User_ID"]
            # Even if user already existed and group already existed insert their roles into the DB
            roleSql = "INSERT INTO " + res.getMembershipTableName() + "(" + res.getMembershipGroupID() + ", " + res.getMembershipRoleID() + ", " + res.getMembershipUserID() + ") VALUES(?,?,?)"
            addEntry = self.sql_operations.nonValueReturningQuery(roleSql,(grpID,x["Role_ID"],usrID))
            if (addEntry):
                pass
            else:
                badReq = True
                break
        if(badReq):
            notFoundResults = jsonify(user_added=userInserted, group_added=groupInserted, role_added = False)
            notFoundResults.status_code = 400
            return notFoundResults
        else:
            successResults = jsonify(user_added=userInserted, group_added=groupInserted, role_added = True)
            successResults.status_code = 200
            return successResults
        
    # @return ERR Request not allowed
    def put(self):
        # Method Stub Uploads are POST Only
        return "PUT Requests are not allow on this endpoint", 400

    # @return ERR Request not allowed
    def delete(self, name):
        # Method Stub Upload is POST Only
        return "DELETE Requests are not allow on this endpoint", 400
