from flask import Flask
from flask_restful import Api
from Users import User

# TODO =
# Parametize SQL queries
# if db exists then nothing else run createTables from db schema

app = Flask(__name__)
api = Api(app)

      
api.add_resource(User, "/user/<string:name>")

app.run(debug=True)