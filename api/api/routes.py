from flask import Flask
from flask_restful import Api
from Users import User, Users
from Groups import Group, Groups
from Roles import Role, Roles
from Membership import Membership, Memberships

# Initialize Flask RESTful API
app = Flask(__name__)
api = Api(app)
# Create endpoints
api.add_resource(Users, "/user")
api.add_resource(User, "/user/<string:name>")
api.add_resource(Groups, "/group")
api.add_resource(Group, "/group/<string:name>")
api.add_resource(Roles, "/role")
api.add_resource(Role, "/role/<string:name>")
api.add_resource(Memberships, "/member")
api.add_resource(Membership, "/member/<int:id>")
# Dev env so lets debug
app.run(debug=True)