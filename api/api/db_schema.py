# @Group Table -> Holds all the groups for the meetings
# @Role Table -> Holds all the Roles a User can have
# @User Table -> Holds all the users
# @Membership Table -> Holds the specific meetings that user are attending with their roles

import sqlite3
import logging

class schema():
    DB_FILE = "jc_meets_db.db"
    DB_NAME = "JC_Meets"
    GRP_TABLE = "Groups"
    GRP_TBL_ID = "Group_ID"
    GRP_TBL_NAME = "Group_Name"
    USR_TBL = "Users"
    USR_TBL_ID = "User_ID"
    USR_TBL_F_NAME = "User_First_Name"
    USR_TBL_L_NAME = "User_Last_Name"
    ROLE_TBL = "Roles"
    ROLE_TBL_ID = "Role_ID"
    ROLE_TBL_DESCRIP = "Role_Descrip"
    ROLE_TBL_NAME = "Role_Name"
    MEM_TBL = "Membership"
    MEM_TBL_USER_ID = "Membership_ID"
    MEM_TBL_GROUP_ID = "Member_Group_ID"
    MEM_TBL_ROLE_ID = "Member_Role_ID"

    # ================================================================================================
    #                           Methods
    #=================================================================================================

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

    # ==================================================================================================
    #                       Getters
    # ==================================================================================================

    def getDatabasePath(self):
        return self.DB_FILE

    def getDatabaseName(self):
        return self.DB_NAME

    def getGroupTableName(self):
        return self.GRP_TABLE

    def getGroupID(self):
        return self.GRP_TBL_ID

    def getGroupName(self):
        return self.GRP_TBL_NAME

    def getUserTableName(self):
        return self.USR_TBL

    def getUserID(self):
        return self.USR_TBL_ID

    def getUserFirstName(self):
        return self.USR_TBL_F_NAME

    def getUserLastName(self):
        return self.USR_TBL_L_NAME

    def getRoleTableName(self):
        return self.ROLE_TBL

    def getRoleID(self):
        return self.ROLE_TBL_ID

    def getRoleName(self):
        return self.ROLE_TBL_NAME

    def getRoleDescrip(self):
        return self.ROLE_TBL_DESCRIP

    def getRoleID(self):
        return self.ROLE_TBL_ID

    def getMembershipTableName(self):
        return self.MEM_TBL

    def getMembershipGroupID(self):
        return self.MEM_TBL_GROUP_ID

    def getMembershipUserID(self):
        return self.MEM_TBL_USER_ID

    def getMembershipRoleID(self):
        return self.MEM_TBL_ROLE_ID
        
    
