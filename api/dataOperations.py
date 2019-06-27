import sqlite3
import logging
from pathlib import Path
from db_schema import schema
import sys

class Initialization(schema):
    # Setup our logger so we can log errors to file
    logging.basicConfig(filename='data-operations-ERR_LOG.log', level=logging.ERROR, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger = logging.getLogger(__name__)

    def __init__(self):       
        # Check for a DB, if we dont have one create one
        if Path(self.DB_FILE).is_file():
            return  None
        else:
            self.createTables()
        return None
    # @return None
    # @descrip - creates tables and populates needed fields for jc-meets
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
        CREATE_MEMBERSHIP_SQL = "CREATE TABLE IF NOT EXISTS " + self. MEM_TBL + " (" + self.MEM_TBL_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + self.MEM_TBL_GROUP_ID + " INTEGER NOT NULL, " + self.MEM_TBL_ROLE_ID + " INTEGER NOT NULL, " + self.MEM_TBL_USER_ID + " INTEGER NOT NULL, FOREIGN KEY(" + self.MEM_TBL_USER_ID + ") REFERENCES " + self.USR_TBL + "(" + self.USR_TBL_ID + ") ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY(" + self.MEM_TBL_ROLE_ID + " ) REFERENCES " + self.ROLE_TBL + " (" + self.ROLE_TBL_ID + ") ON UPDATE CASCADE ON DELETE CASCADE,FOREIGN KEY(" + self.MEM_TBL_GROUP_ID + ") REFERENCES " + self.GRP_TBL + "(" + self.GRP_TBL_ID + ") ON UPDATE CASCADE ON DELETE CASCADE);"
        # Populate Bridge table
        INSERT_MEM_SQL = "INSERT INTO " + self.MEM_TBL + "(" + self.MEM_TBL_GROUP_ID + ", " + self.MEM_TBL_ROLE_ID + ", " + self.MEM_TBL_USER_ID + ") VALUES(?,?,?)"
        try:
            # Spin up some sweet pseudo information
            fakeGroups = [("Software Group"),("Hardware Group"),("DevOps Group"),("Embeded Group")]
            fakeRoles = [("Leads the group presentation", "Presenter"),("Person thats attending group","Particpant"),("Person that plans group activities","Organizer")]
            fakeUsers = [("Justin", "Collier" ),("Brent","Burkey"),("Kay","Krivolavek"),("Derek","Bringewatt")]
            fakeMembership = [(1,2,1),(1,2,2),(1,3,3),(1,1,4),(2,3,1),(2,1,2),(2,2,3),(2,2,4),(3,2,1),(3,3,2),(3,2,3),(3,1,4),(4,1,1),(4,2,2),(4,2,3),(4,3,4)]
            # Connect
            conn = sqlite3.connect(self.DB_FILE)
            c = conn.cursor()
            # Create Tables
            c.execute(CREATE_GROUP_SQL)
            c.execute(CREATE_USERS_SQL)
            c.execute(CREATE_MEMBERSHIP_SQL)
            c.execute(CREATE_ROLES_SQL)
            # Populate Tables
            for x in fakeGroups:
                c.execute(INSERT_GROUP_SQL,(x,))  
            for x in fakeRoles:
                c.execute(INSERT_ROLE_SQL,(x))
            for x in fakeUsers:
                c.execute(INSERT_USERS_SQL,(x))
            for x in fakeMembership:
                c.execute(INSERT_MEM_SQL,(x))
            conn.commit()
        except Exception as e:
            # Catch general exception and write to file
            self.logger.error(e)
        finally:
            conn.close()
        return None

class SQL_Operations(schema):
    # Setup our logger so we can log errors to file
    logging.basicConfig(filename='data-operations-ERR_LOG.log', level=logging.ERROR, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger = logging.getLogger(__name__)

    def __init__(self):
        return None

    # setup our results so we have row names as JSON ids, and row results as JSON keys
    def make_dicts(self, cursor, row):
        return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

    # @params SQL - str, valid SQL Statement
    # @params SQL_Params - tuple, valid SQL Parameter. For only one parameter make sure to include comma after
    # @return JSON dict of the SQL Query
    def valueReturningQuery(self, SQL, SQL_Params):        
        try:
            conn = sqlite3.connect(self.DB_FILE)
            conn.row_factory = self.make_dicts 
            c = conn.cursor()
            c.execute(SQL, SQL_Params)
            results = c.fetchall()
        except Exception as e:
            results = None
            # Catch general exception and write to file
            self.logger.error(e)
        finally:
            conn.close()
        return results

    # @params  SQL - str, valid SQL Statement
    # @params SQL_Params - tuple, valid SQL Paramter. For only one parameter make sure to include comma after first field
    # @return Boolean - true if operation succeeded , false if operation failed
    def nonValueReturningQuery(self, SQL, SQL_Params):
        try:
            conn = sqlite3.connect(self.DB_FILE)
            c = conn.cursor()
            c.execute(SQL, SQL_Params)
            # Even if we have valid SQL query, we may not modifiy any data. Make sure we have modified data
            # before sending back a true flag
            if(c.rowcount > 0):
                conn.commit()
                results = True
            else:
                raise Exception('Not a Valid SQL Statement') 
        except Exception as e:
            results = False
            # Catch general exception and write to file
            self.logger.error(e)
        finally:
            conn.close()
        return results

    # @params  table - str, valid SQL table
    # @params whereArg - str, condtional column name
    # @params whereParams - str, value to be checked
    # @return Boolean - true if operation succeeded , false if operation failed
    def ifExistsQuery(self, table, whereArg, whereParam):
        try:
            conn = sqlite3.connect(self.DB_FILE)
            c = conn.cursor()
            c.execute("SELECT EXISTS(SELECT 1 FROM "+ table + " WHERE "+ whereArg + " = '"+ whereParam + "' LIMIT 1);")
            # Even if we have valid SQL query, we may not modifiy any data. Make sure we have modified data
            # before sending back a true flag
            queryResults = c.fetchone()
            if(queryResults[0] == 1):
                results = True
            else:
                raise Exception('Not a Valid SQL Statement') 
        except Exception as e:
            results = False
            # Catch general exception and write to file
            self.logger.error(e)
        finally:
            conn.close()
        return results
