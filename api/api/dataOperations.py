import sqlite3
import logging
from pathlib import Path
from db_schema import schema
import sys

class Initialization(schema):
    def __init__(self):       
        # Check for a DB, if we dont have one create one
        if Path(self.DB_FILE).is_file():
            return  None
        else:
            self.createTables()
        return None

    def createTables(self):
        # Create Groups
        CREATE_GROUP_SQL = "CREATE TABLE IF NOT EXISTS " + self.GRP_TBL + " (" + self.GRP_TBL_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + self.GRP_TBL_NAME + " TEXT NOT NULL);" 
        # Populate Groups
        INSERT_GROUP_SQL = "INSERT INTO " + self.GRP_TBL + "(" + self.GRP_TBL_NAME + ") VALUES(?)"
        # Create Users
        CREATE_USERS_SQL = "CREATE TABLE IF NOT EXISTS " + self.USR_TBL + " (" + self.USR_TBL_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + self.USR_TBL_F_NAME + " text NOT NULL, " + self.USR_TBL_L_NAME + " text); "
        # Populate Users
        INSERT_USERS_SQL = "INSERT INTO " + self.USR_TBL + "(" + self.USR_TBL_F_NAME + ", " + self.USR_TBL_L_NAME+ ") VALUES(?,?)"
        # Create Roles
        CREATE_ROLES_SQL = "CREATE TABLE IF NOT EXISTS " + self.ROLE_TBL + " (" + self.ROLE_TBL_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + self.ROLE_TBL_DESCRIP + " text, " + self.ROLE_TBL_NAME + " text NOT NULL); "
        # Populate Roles
        INSERT_ROLE_SQL = "INSERT INTO " + self.ROLE_TBL + "(" + self.ROLE_TBL_DESCRIP + ", " + self.ROLE_TBL_NAME + ") VALUES(?,?)"
        # Create Membership Bridge Table
        CREATE_MEMBERSHIP_SQL = "CREATE TABLE IF NOT EXISTS " + self. MEM_TBL + " (" + self.MEM_TBL_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + self.MEM_TBL_GROUP_ID + " INTEGER NOT NULL, " + self.MEM_TBL_ROLE_ID + " INTEGER NOT NULL, " + self.MEM_TBL_USER_ID + " INTEGER NOT NULL);"
        # Populate Bridge table
        INSERT_MEM_SQL = "INSERT INTO " + self.MEM_TBL + "(" + self.MEM_TBL_GROUP_ID + ", " + self.MEM_TBL_ROLE_ID + ", " + self.MEM_TBL_USER_ID + ") VALUES(?,?,?)"
        try:
            # Spin up some sweet pseudo information
            fakeGroups = ("Group One",)
            fakeRoles = ("Role Description", "Presenter")
            fakeUsers = ("Richie", "Thomas" )
            fakeMembership = (1,1,1)
            # Connect
            conn = sqlite3.connect(self.DB_FILE)
            c = conn.cursor()
            # Create Tables
            c.execute(CREATE_GROUP_SQL)
            c.execute(CREATE_USERS_SQL)
            c.execute(CREATE_MEMBERSHIP_SQL)
            c.execute(CREATE_ROLES_SQL)
            # Populate Tables
            c.execute(INSERT_GROUP_SQL,fakeGroups)
            c.execute(INSERT_ROLE_SQL, fakeRoles)
            c.execute(INSERT_USERS_SQL, fakeUsers)
            c.execute(INSERT_MEM_SQL, fakeMembership)
            conn.commit()
        except Exception as e:
            print(e, file=sys.stderr)
        finally:
            conn.close()
        return None

class SQL_Operations(schema):

    def __init__(self):
        return None

    # setup our results so we have row names as JSON ids, and row results as JSON keys
    def make_dicts(self, cursor, row):
        return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

    def valueReturningQuery(self, SQL):        
        try:
            conn = sqlite3.connect(self.DB_FILE)
            conn.row_factory = self.make_dicts 
            c = conn.cursor()
            c.execute(SQL)
            results = c.fetchall()
        except Exception as e:
            results = None
            print(e)
        finally:
            conn.close()
        return results

    def nonValueReturningQuery(self, SQL):
        try:
            conn = sqlite3.connect(self.DB_FILE)
            c = conn.cursor()
            c.execute(SQL)
            conn.commit()
            results = True
        except Exception as e:
            results = False
            print(e, file=sys.stderr)
        finally:
            conn.close()

        return results
