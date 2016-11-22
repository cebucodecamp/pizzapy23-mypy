from typing import NewType

DBName = NewType('DBName', str)


# access documents in a database, for example Mongo:
def open_database(name: DBName):
    print("Opening database {}".format(name))


db_name = DBName("users")

open_database(db_name)
open_database("user")
