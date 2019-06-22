import sqlite3
import logging
from db_schema import schema

class Initialization(schema):
    CREATE_GROUP_SQL = "CREATE TABLE IF NOT EXISTS " + GRP_TBL + " (" 
    GRP_TBL_ID + " integer PRIMARY KEY, "
    GRP_TBL_NAME + " text NOT NULL);" 

    CREATE_USERS_SQL = "CREATE TABLE IF NOT EXISTS " + USR_TBL + " (" 
    USR_TBL_ID + " integer PRIMARY KEY, "
    USR_TBL_F_NAME + " text NOT NULL, "
    USR_TBL_L_NAME + " text); "

    CREATE_ROLES_SQL = "CREATE TABLE IF NOT EXISTS " + ROLE_TBL + " (" 
    ROLE_TBL_ID + " integer PRIMARY KEY, "
    ROLE_TBL_DESCRIP + " text, "
    ROLE_TBL_NAME + " text NOT NULL); "

    CREATE_MEMBERSHIP_SQL = "CREATE TABLE IF NOT EXISTS " + MEM_TBL + " (" 
    MEM_TBL_ID + " integer PRIMARY KEY, "
    MEM_TBL_GROUP_ID + " integer NOT NULL, "
    MEM_TBL_ROLE_ID + " integer NOT NULL "
    MEM_TBL_USER_ID + " integer NOT NULL);"

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

class SQL_Operations(schema):

    def __init__(self):
        return None

    def valueReturningQuery(self, SQL):        
        try:
            conn = sqlite3.connect(self.DB_FILE)
            c = conn.cursor()
            c.execute(SQL)
            rows = c.fetchall()
        except Error as e:
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
            results = True
        except Error as e:
            results = False
            print(e)
        finally:
            conn.close()

        return results
