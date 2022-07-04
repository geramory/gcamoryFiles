import classfile            # can use Alias rename charFile as an
import re
from pymongo import MongoClient
import pprint
import logging  # Add logs to a file


# Used to create user object from inputted values
logging.basicConfig(filename = 'users.log', level = logging.DEBUG, format = '%(asctime)s %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p::')
    
def add_user() -> classfile.User:                     
    while True:
        try:      
            print("\nGreetings! Please select type of transaction to input:")
            print("\t a.) CD")
            print("\t b.) Deposit")
        
            typeUser = input()
            CDfunds = 10000               # CDfunds initialize
            DEPOSITfunds = 500            # DEPOSITfunds intialize
            
            # Input verification
            if not typeUser == 'a' and not typeUser == 'c' and not typeUser == 'b':
                raise ValueError('Invalid input for transaction type')
            else:
                break

        except ValueError:
            print("Oh no! Please enter a valid type for user-->('a', 'c')")
            

    while True:
        try:
            print("\n\nPlease Enter your name:")
            name = input()
            if not re.search(",", name) == None:     # used REGEX here other restrictions: (r"[,\.\\\*\-]", name)
                raise ValueError
            else:
                break
        except ValueError:
            print("Please do not use a ',' in your application! ")


    while True:
        try:
            print("\n\nEnter your funding amount:")
            funds = int(input())
            
            


            break
        except ValueError:
            print("Please enter a number for your amount. Try again.")


    if typeUser == 'a':
        newuser = classfile.Money(name, funds + CDfunds) 

    elif typeUser == 'b':
        newuser = classfile.Debit(name, funds + DEPOSITfunds)

    else:
        newuser = classfile.User(name, funds)
    
    return newuser



def saved_Users(lst_Users):     # Save the user list to this file, easy to import it
    f = open('saved_Users.txt', 'w')  

    for charFile in lst_Users:
        f.write(classfile.name + "," + str(classfile.funds) + "," + classfile.Transaction_type + "\n") # str = convert int to string, also use str(type(charFile))
        
    f.close()

# Load users from saved_Users.txt file
def load_Users():
    f = open('saved_Users.txt', 'r')
    lst_ofusers = []
    for line in f:            # for loop, to loop through all the lines in the file
        if line == '':        # There is an empty line in saved_users.txt on line 4
            break

        user_data = line.split(",")     # SPLIT function can convert lines of code seperated by commas into a list to use its indexes
        print(user_data[2])             # has white space inbetween  user_data[2] = Deposit type 
        if user_data[2].strip() == 'CD':                             # .strip() gets rid of white space or \n characters
            newuser = classfile.Money(user_data[0], user_data[1])

        elif user_data[2].strip() == 'Deposit':
            newuser = classfile.Debit(user_data[0], user_data[1])

        else:
            newuser = classfile.User(user_data[0], user_data[1])
            
        lst_ofusers.append(newuser)
    f.close()


    return lst_ofusers


# Function to save an user to collection in MongoDB
def save_to_db(person, bankdb):
    logging.debug("Entering save_to_db")
    dict_User = {
        "name" : person.name,  # ---> Database information
        "funds" : person.funds,
        "type" : person.type
    }

    bankdb.users.insert_one(dict_User)    # Insert into database, user collection in bank database
    logging.info("Successfully added an object to the database")


def log():        # Print out activity log to user

    f1 = open('users.log', 'r')
    
    for line in f1: 
        print(line)

    f1.close()



def set1():        # Drop database function


    client = MongoClient()   

    bankdb = client.pyproject

    movies = bankdb.users  

    movies.drop()   
    
    
set1()
  


# Main function
def main():

    client = MongoClient()   

    bankdb = client.pyproject


    lst_Users = load_Users()                   


    while True:
        print("\n\n\t\t    Welcome to the Money Bank!\n")
        print("\t\t##################################")
        print("\t\t FREE sign-on BONUS for all users")
        print("\t\t   CD: $10000  SAVINGS: $500")
        print("\t\t##################################\n")
        print("\t\t     Please make a selection:")
        print("\na.) Create new user")
        print("s.) Save bank statement to MongoDB")
        print("l.) View activity logs")
        print("d.) UPDATE DataBase")
        print("z.) Drop DataBase")
        print("c.) Cancel transaction")

        option = input()

        logging.debug("User inputed %s", option)        # User input q logged option in users.log

        if option == 'c':
            print("\t\tThank you for your business, Have a nice day!\n")
            break
        elif option == 'z':
            set1()
        elif option =='s':
            for person in lst_Users:                     # MONGODB added 'for' loop
                save_to_db(person, bankdb)
        elif option == 'l':
            log()
        elif option == 'a':
            lst_Users.append(add_user())             # adds Saved users to the file list
        else:
            print("invalid selection! Please try again!")
    
    for classfile in lst_Users:
        print(classfile, type(classfile))

    saved_Users(lst_Users)

#if __name__ == '__main__':  
main()