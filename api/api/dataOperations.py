import sqlite3
import logging
from db_schema import schema

class Initialization(schema):
    CREATE_GROUP_SQL =""
    CREATE_USERS_SQL = ""
    CREATE_ROLES_SQL = ""
    CREATE_MEMBERSHIP_SQL = ""
    INSERT_GROUP_SQL = ""
    INSERT_ROLE_SQL = ""
    INSERT_USERS_SQL = ""
    INSERT_ROLES_SQL = ""
    
    def __init__(self):        
        return None

    def createTables(self):
        try:
            conn = sqlite3.connect(self.DB_FILE)
            c = conn.cursor()
            # Create Tables
            c.execute(self.CREATE_GROUP_SQL)
            c.execute(self.CREATE_USERS_SQL)
            c.execute(self.CREATE_MEMBERSHIP_SQL)
            c.execute(self.CREATE_ROLES_SQL)
            # Populate Tables
            c.execute(self.INSERT_GROUP_SQL)
            c.execute(self.INSERT_ROLE_SQL)
            c.execute(self.INSERT_USERS_SQL)
            c.execute(self.CREATE_MEMBERSHIP_SQL)
        except Error as e:
            print(e)
        finally:
            conn.close()
        return None

class SQL_Operations(object):

