# import the sqlite3 database module
import sqlite3
from contextlib import closing


def setup_database(conn):
    cursor = conn.cursor()
    # create the table if it doesn't already exist
    # note that primary keys are automatically created in sqlit3 and referenced as rowid 
    cursor.execute("CREATE TABLE IF NOT EXISTS mcu_superheroes (first_name TEXT, last_name TEXT, alias TEXT, species TEXT, citizenship TEXT, birth_year TEXT, status TEXT, portrayed_by TEXT)")

    # create some records of data
    cursor.execute("INSERT INTO mcu_superheroes VALUES ('Tony', 'Stark', 'Iron Man', 'Human', 'American', '1970', 'Deceased', 'Robert Downey, Jr.')")
    cursor.execute("INSERT INTO mcu_superheroes VALUES ('Carol', 'Danvers', 'Captain Marvel', 'Human/Kree Hybrid', 'American / Kree Imperial (formerly)', '1964', 'Alive', 'Brie Larson')")
    cursor.execute("INSERT INTO mcu_superheroes VALUES ('Sersi', '', 'N/A', 'Eternal', 'British', 'Before 5000 BC', 'Alive', 'Gemma Chan')")
    cursor.execute("INSERT INTO mcu_superheroes VALUES ('Shang-Chi', 'Xu', 'N/A', 'Human', 'Chinese (formerly) / American', '1999', 'Alive', 'Simu Liu')")

def list_name_and_alias(conn):
    cursor = conn.cursor()
    print("Superheroes and their aliases")
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, alias FROM mcu_superheroes")

    # store the results of a the query to a list called superheroess
    superheroes = cursor.fetchall()

    # now we can loop through the results of the query
    for this_superhero in superheroes:
      print(this_superhero[0], this_superhero[1], this_superhero[2], this_superhero[3])

def list_species_and_citizenship(conn):
    print("Superheroes and their species and citizenship")
    cursor = conn.cursor()
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, species, citizenship FROM mcu_superheroes")

    # store the results of a the query to a list called superheroes
    superheroes = cursor.fetchall()

    # now we can loop through the results of the query
    for this_superhero in superheroes:
      print(this_superhero[0], this_superhero[1], this_superhero[2], this_superhero[3], this_superhero[4])

def list_birth_year_and_status(conn):
    print("Superheroes and their birth year and status")
    cursor = conn.cursor()
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, birth_year, status FROM mcu_superheroes")

    # store the results of a the query to a list called superheroess
    superheroes = cursor.fetchall()

    # now we can loop through the results of the query
    for this_superhero in superheroes:
      print(this_superhero[0], this_superhero[1], this_superhero[2], this_superhero[3], this_superhero[4])

def list_portrayed_by(conn):
    print("Superheroes and the actors/actresses who portray them")
    cursor = conn.cursor()
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, portrayed_by FROM mcu_superheroes")

    # store the results of a the query to a list called superheroess
    superheroes = cursor.fetchall()

    # now we can loop through the results of the query
    for this_superhero in superheroes:
      print(this_superhero[0], this_superhero[1], this_superhero[2], this_superhero[3])

def add_new_superhero(conn):
    print("Let's add new MCU superhero to the database with some instructions below:\n")
    print("If you know that the superhero doesn't have either first name or last name, \nplease leave it empty!")
    print("If you know that the superhero doesn't possess any attributes \n(other than first name and last name), please input \"N/A\"!")
    print("If you're not sure about any attributes \n(other than first name and last name), please input \"Not sure\"!")
    print()

    cursor = conn.cursor()

    input_first_name = input("First name: ")
    input_last_name = input("Last name: ")
    input_alias = input("Alias: ")
    input_species = input("Species: ")
    input_citizenship = input("Citizenship: ")
    input_birth_year = input("Birth year: ")
    input_status = input("Status: ")
    input_portrayed_by = input("Portrayed by: ")

    # prepare your insert statement using ? for each item that you will insert
    sql = """"
        INSERT INTO mcu_superheroes (first_name, last_name, alias, species, citizenship, birth_year, status, portrayed_by)
        VALUE (?,?,?,?,?,?,?,?)
        """

    cursor.execute(sql, (input_first_name, input_last_name, input_alias, input_species, input_citizenship, input_birth_year, input_status, input_portrayed_by))

    print("Superhero added. Thank you!")


def display_menu():
    print()
    print("* * * * * * * COMMAND MENU * * * * * * *")
    print("1 - List superheroes and their alias")
    print("2 - List superheroes and their species and citizenship")
    print("3 - List superheroes and their birth year and status")
    print("4 - List superheroes and actors/actresses who portray them")
    print("5 - Add new superhero to the database")
    print("6 - Exit the program")

def main():
    print("Welcome to MCU Superheroes Database")

    # create a connection to the database file
    conn = sqlite3.connect("myDatabase.db")

    setup_database(conn)
    while True:
        display_menu()
        print()
        command = input("Command: ")
        print()
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
    print("Thank you for using MCU superhero database. See you later for more interesting about Marvel Cinematic Universe!")

if __name__ == "__main__":
    main()