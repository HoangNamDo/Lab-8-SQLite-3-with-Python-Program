# import the sqlite3 database module
import sqlite3

print("SQLite Practice - Example User Table\n")
# create a connection to the database file
conn = sqlite3.connect("myDatabase.db")

# create a cursor that we will use to move through the database 
cursor = conn.cursor()

# create the table if it doesn't already exist
# note that primary keys are automatically created in sqlit3 and referenced as rowid 
cursor.execute("CREATE TABLE IF NOT EXISTS user (first_name TEXT, last_name TEXT, email TEXT, phone_number TEXT, street_address TEXT, city TEXT, state TEXT, zipcode TEXT)")

# create some records of data
cursor.execute("INSERT INTO user VALUES (\"Tony\", \"Stark\", \"ironman@avengers.com\", \"324-557-9685\", \"200 Park Avenue\", \"New York\", \"NY\", \"10166\")")
cursor.execute("INSERT INTO user VALUES (\"Carol\", \"Danvers\", \"captainmarvel@avengers.com\", \"201-422-7560\", \"3716 Liberty Ave\", \"North Bergen\", \"NJ\", \"07047\")")

# query the table including the rowid primary key value
cursor.execute("SELECT rowid, first_name, last_name, email, phone_number, street_address, city, state, zipcode FROM user")

# store the results of a the query to a list called users
users = cursor.fetchall()


# now we can loop through the results of the query
for this_user in users:
  print(this_user[0], this_user[1], this_user[2], this_user[3], this_user[4], this_user[5], this_user[6], this_user[7], this_user[8])

# save the updates to the database - if you don't commit any updates/inserts to the database will not be saved
conn.commit()

# close the connection
conn.close()


def display_menu():
    print("Welcome to the MARVEL Universe database\n")
    print("* * * MENU * * *")
    print("COMMAND MENU")
    print("1 - List all NAMES in the user table")
    print("2 - List NAMES and email/phone for all users")
    print("3 - List NAMES and city/state for all users")
    print("4 - Add new User")
    print("5 - Exit the program")

def main():
    display_menu()
    while True:
        print()
        command = input("Command: ").lower()
        if command == "1":
            list_names(user)
        elif command == "2":
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()