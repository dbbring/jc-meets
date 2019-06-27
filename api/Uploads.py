from flask_restful import Resource, reqparse, request
from flask import jsonify
from dataOperations import Initialization, SQL_Operations
from db_schema import schema
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
        parser = reqparse.RequestParser()
        parser.add_argument("Group_Name")
        args = parser.parse_args()
        print(request.get_json(), file=sys.stderr)
        sql = "INSERT INTO " + res.getGroupTableName() + " (" + res.getGroupName() +") VALUES (?);"
        # Parameterized SQL (Remember comma after parameter since we only have one parameter)
        insertResults = self.sql_operations.nonValueReturningQuery(sql,(args["Group_Name"],))
        if (insertResults):
            # JSONify our results
            succesfulResults = jsonify(inserted=True)
            succesfulResults.status_code = 201
            return succesfulResults
        badResults = jsonify(inserted=False)
        badResults.status_code = 400
        return badResults

    # @return ERR Request not allowed
    def put(self):
        # Method Stub Uploads are POST Only
        return "PUT Requests are not allow on this endpoint", 400

    # @return ERR Request not allowed
    def delete(self, name):
        # Method Stub Upload is POST Only
        return "DELETE Requests are not allow on this endpoint", 400
