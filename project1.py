
import charFile            # can use Alias rename charFile as an
import re
from pymongo import MongoClient
import pprint
import logging  # Add logs to a file


# Used to create animal object from user-inputted values
logging.basicConfig(filename = 'users.log', level = logging.DEBUG, format = '%(asctime)s %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p::')
    
def add_user() -> charFile.User:                     
    while True:
        try:      
            print("\nGreetings! Please select type of transaction to input:")
            print("\t a.) CD")
            print("\t b.) Deposit")
        
            typeUser = input()
            CDfunds = 10000
            DEPOSITfunds = 500

            # Input verification
            if not typeUser == 'a' and not typeUser == 'c' and not typeUser == 'b':
                raise ValueError('Invalid input for transaction type')
            else:
                break

        except ValueError:
            print("Oh no! Please enter a valid type for animal-->('a', 'c')")
            

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
        newuser = charFile.Money(name, funds + CDfunds) 

    elif typeUser == 'b':
        newuser = charFile.Debit(name, funds + DEPOSITfunds)

    else:
        newuser = charFile.User(name, funds)
    
    return newuser



def saved_Users(lst_Users):     # Save the user list to this file, easy to import it
    f = open('saved_Users.txt', 'w')  

    for charFile in lst_Users:
        f.write(charFile.name + "," + str(charFile.funds) + "," + charFile.Transaction_type + "\n") # str = convert int to string, also use str(type(charFile))
        
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
            newuser = charFile.Money(user_data[0], user_data[1])
        elif user_data[2].strip() == 'Deposit':
            newuser = charFile.Debit(user_data[0], user_data[1])
        else:
            newuser = charFile.User(user_data[0], user_data[1])
            
        lst_ofusers.append(newuser)
    f.close()


    return lst_ofusers


# Function to save an animal to collection in MongoDB
def save_to_db(person, animaldb):
    logging.debug("Entering save_to_db")
    dict_User = {
        "name" : person.name,  # ---> Database information
        "funds" : person.funds,
        "type" : person.type
    }

    animaldb.animals.insert_one(dict_User)    # Insert into database, animal collection in animal database
    logging.info("Successfully added an object to the database")


# Main function
def main():
    #print("\n\n\t\tWelcome to the Money Bank!")

    client = MongoClient()   

    animaldb = client.animals

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
        print("d.) View DataBase")
        print("z.) Drop DataBase")
        print("c.) Cancel transaction")

        option = input()

        logging.debug("User inputed %s", option)        # User input q logged option in users.log

        if option == 'c':
            print("\t\tThank you for your business, Have a nice day!\n")
            break
        elif option =='s':
            for person in lst_Users:                     # MONGODB added 'for' loop
                save_to_db(person, animaldb)
        elif option == 'a':
            lst_Users.append(add_user())             # adds Saved users to the file list
        else:
            print("invalid selection! Please try again!")
    
    for charFile in lst_Users:
        print(charFile, type(charFile))

    saved_Users(lst_Users)

#if __name__ == '__main__':  
main()