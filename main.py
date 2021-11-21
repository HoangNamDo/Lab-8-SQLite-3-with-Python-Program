# import the sqlite3 database module
import sqlite3

def setup_database(conn):
    cursor = conn.cursor()
    # create the table if it doesn't already exist
    # note that primary keys are automatically created in sqlit3 and referenced as rowid 
    cursor.execute("CREATE TABLE IF NOT EXISTS superheroes (first_name TEXT, last_name TEXT, alias TEXT, species TEXT, citizenship TEXT, birth_year TEXT, status TEXT, portrayed_by TEXT)")

    # create some records of data
    cursor.execute("INSERT INTO superheroes VALUES ('Tony', 'Stark', 'Iron Man', 'Human', 'American', '1970', 'Deceased', 'Robert Downey, Jr.')")
    cursor.execute("INSERT INTO superheroes VALUES ('Carol', 'Danvers', 'Captain Marvel', 'Human/Kree Hybrid', 'American/Kree Imperial (formerly)', '1964', 'Alive', 'Brie Larson')")
    cursor.execute("INSERT INTO superheroes VALUES ('Sersi', 'N/A', 'N/A', 'Eternal', 'British', 'Before 5000 BC', 'Alive', 'Gemma Chan')")
    cursor.execute("INSERT INTO superheroes VALUES ('Shang-Chi', 'Xu', 'N/A', 'Human', 'Chinese (formerly)/American', '1999', 'Alive', 'Simu Liu')")

def list_name_and_alias(conn):
    cursor = conn.cursor()
    print("All superheroes currently in the database")
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, alias FROM superheroes")

    # store the results of a the query to a list called superheroess
    superheroess = cursor.fetchall()

    # now we can loop through the results of the query
    for this_superhero in superheroess:
      print(this_superhero[0], this_superhero[1], this_superhero[2])

def list_species_and_citizenship(conn):
    cursor = conn.cursor()
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, species, citizenship FROM superheroes")

    # store the results of a the query to a list called superheroess
    superheroes = cursor.fetchall()

    # now we can loop through the results of the query
    for this_superhero in superheroes:
      print(this_superhero[0], this_superhero[3], this_superhero[4])

def list_birth_year_and_status(conn):
    cursor = conn.cursor()
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, species, citizenship, birth_year FROM superheroes")

    # store the results of a the query to a list called superheroess
    superheroes = cursor.fetchall()

    # now we can loop through the results of the query
    for this_superhero in superheroes:
      print(this_superhero[0], this_superhero[3], this_superhero[4], this_superhero[5])

def list_portrayed_by(conn):
    cursor = conn.cursor()
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, portrayed_by FROM superheroes")

    # store the results of a the query to a list called superheroess
    superheroes = cursor.fetchall()

    # now we can loop through the results of the query
    for this_superhero in superheroes:
      print(this_superhero[0], this_superhero[8])

def add_new_superhero(conn):
    print("Add new superhero\n")
    print("If superhero doesn't have first name or last name, please leave it empty!")
    print("If superhero doesn't have alias, please input 'N/A'!")
    input_first_name = input("First name: ")
    input_last_name = input("Last name: ")
    input_alias = input("Alias: ")
    input_birthyear = input("Birth year: ")


def display_menu():
    print("Welcome to MCU Superheroes Database\n")
    print("* * * COMMAND MENU * * *")
    print("1 - List superheroes' first name, last name, and alias")
    print("2 - List superheroes' species and citizenship")
    print("3 - List superheroes' birth year and status")
    print("4 - List actors/actresses whom superhero portrayed by")
    print("5 - Add new superhero to the database")
    print("6 - Exit the program")

def main():
    print("SQLite Practice - Example superheroes Table\n")
    # create a connection to the database file
    conn = sqlite3.connect("myDatabase.db")
    # create a cursor that we will use to move through the database 
    # cursor = conn.cursor()
    setup_database(conn)
    while True:
        display_menu()
        print()
        command = input("Command: ").lower()
        if command == "1":
            list_name_and_alias(conn)
        elif command == "2":
            list_species_and_citizenship(conn)
        elif command == "3":
            list_birth_year_and_status(conn)
        elif command == "4":
            list_portrayed_by(conn)
        elif command == "5":
            add_new_superhero(conn)
        elif command == "6":
            break
        else:
            print("Unknown command. Please try again.")
    # save the updates to the database - if you don't commit any updates/inserts to the database will not be saved
    conn.commit()
    # close the connection
    conn.close()
    # farewell message
    print("Thank you for accessing MCU superhero database.")

if __name__ == "__main__":
    main()