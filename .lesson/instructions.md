# Practice Lab 8

Using the starting code file, build upon the program by doing the following:


* Add a program title and consider the user experience throughout your output. 


* Modify the user table and create columns/fields to store the following information: first name, last name, email address, phone number, street address, city, state, zipcode. 


* Populate your table with at least 5 records of unique data. Feel free to keep to a theme like I have (Marvel) or whatever theme you would like. 


* Create a menu for the user to interact with your data by creating functions that will perform different SQL SELECT queries. 


* Create two report functions of your choice and comfort level. Some suggestions for report functions include listing all users first and last names, or creating a list of names and contact information. Create an associated item in the menu so the program user can run these reports. 


* Build an Add User function that asks for input for the following fields and inserts a new record/row of data into your SQLite database. Be sure to add this function to the program menu.

        * first name
        * last name
        * email address
        * phone number
        * street address
        * city
        * state
        * zipcode

* Use your Add User function within the program to add 5 more user records to your database.


* After having 10 users in your database table, test your report functions and make sure your data is printing out properly.


* Be sure to include an option to EXIT the program. The program user should be able to keep working with the menu after every option until they choose to exit the program.
---
## Tips
Remove any reference to DROP the user table. We want our user table to persist and not be wiped clean every time we run the program. 

Make sure that you only create the user table once by writing your query like this:
```
CREATE TABLE IF NOT EXISTS user
```

Test that your user input exists in the database even after you stop and rerun the program. The data should be persistent. 

Note: You do not have to validate the user input for this activity. You can if you want to, but it is not required. 

## Example output
```
Welcome to the MARVEL Universe database

* * * MENU * * * 
1 - List all NAMES in the user table
2 - List NAMES and email/phone for all users
3 - List NAMES and city/state for all users
4 - Add new User
5 - Exit the program

Your choice: 1

All NAMES in the USER table
* * * * * * * * * * * * * *
Carol Danvers
Tony Stark

* * * MENU * * * 
1 - List all NAMES in the user table
2 - List NAMES and email/phone for all users
3 - List NAMES and city/state for all users
4 - Add new User
5 - Exit the program

Your choice: 2

NAMES and email/phone for all USERS
* * * * * * * * * * * * * *
Carol Danvers   carol@marvel.com  555-222-1111
Tony Stark      tony@marvel.com   555-222-1234

* * * MENU * * * 
1 - List all NAMES in the user table
2 - List NAMES and email/phone for all users
3 - List NAMES and city/state for all users
4 - Add new User
5 - Exit the program

Your choice: 3

NAMES and city/state for all USERS
* * * * * * * * * * * * * *
Carol Danvers   Boston, MA
Tony Stark      Malibu, CA

* * * MENU * * * 
1 - List all NAMES in the user table
2 - List NAMES and email/phone for all users
3 - List NAMES and city/state for all users
4 - Add new User
5 - Exit the program

Your choice: 4

Add New USER
* * * * * * * 
Enter first name: Bruce
Enter last name: Banner
Enter email address: bruce@marvel.com
Enter phone number: 555-111-2233
Enter street address: 123 Main Street
Enter city: Dayton
Enter 2 digit state abbreviation: OH
Enter zipcode: 45377

Bruce Banner has been entered into the USER table.


* * * MENU * * * 
1 - List all NAMES in the user table
2 - List NAMES and email/phone for all users
3 - List NAMES and city/state for all users
4 - Add new User
5 - Exit the program

Your choice: 5

Thank you for using this program.
```