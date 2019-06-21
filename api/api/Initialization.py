from flask_restful import Resource, reqparse
import sqlite3
from sqlite3 import Error
from db_schema import schema

class Initialization(schema):
    users = [
        {
            "name": "Nicholas",
            "age": 42,
            "occupation": "Network Engineer"
        },
        {
            "name": "Elvin",
            "age": 32,
            "occupation": "Doctor"
        },
        {
            "name": "Jass",
            "age": 22,
            "occupation": "Web Developer"
        }
    ]

    def __init__(self):
        return 

    def create_connection(db_file):
        #""" create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            conn.close()

    def create_table(conn, create_table_sql):
        #""" create a table from the create_table_sql statement
        #:param conn: Connection object
        #:param create_table_sql: a CREATE TABLE statement
        #:return:
        #"""
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)



    def get(self, name):
        create_connection("C:\\sqlite\db\pythonsqlite.db")
        for user in self.users:
            if(name == user["name"]):
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
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200