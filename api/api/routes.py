from flask import Flask
from flask_restful import Api
from Users import User, Users
from Groups import Group, Groups

# TODO =
# Add in Forgein keys then delete DB then re create
# make data singleton class?
# if db exists then nothing else run createTables from db schema

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, "/user")
api.add_resource(User, "/user/<string:name>")
api.add_resource(Groups, "/group")
api.add_resource(Group, "/group/<string:name>")

app.run(debug=True)