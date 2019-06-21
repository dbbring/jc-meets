from db_schema import schema

class test(schema):

    def __init__(self):
        return

    

tester = test()
tester.setTableName("newTable")

print(tester.TABLE_NAME)
