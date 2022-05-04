
class User:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

# Child class
class bank(User):
    total_deposits = 0
    total_withdraws = 0

    def __init__(self, name, occupation, balance):
        super().__init__(name, occupation)
        self.balance = balance

    def show_info(self):
        return f"{self.name} has a remaining balance of: ${round(self.balance, 2)}\n\n\n"

    def deposit(self):
        dep = float(input(f"{self.name}, please enter how much you would like to deposit: "))
        print("Deposit transaction completed.\n\n")
        self.balance = self.balance + dep
        self.total_deposits = self.total_deposits + 1
        return f"Your balance is : ${round(self.balance, 2)}"

    def withdraws(self):
        witd = float(input(f"{self.name}, please enter how much you would like to withdraw: "))
        if self.balance < witd:
            return "Insufficient Funds!"
        else:
            print("Withdraw transaction completed.\n\n")
            self.balance = self.balance - witd
            self.total_withdraws = self.total_withdraws + 1
            return f"Your balance is: ${round(self.balance, 2)}"

def options(user_one):
    print("\nThank you for creating a new bank account")
    print("Here is a list of options, please choose from the following:\n")

    while True:

        option_choice = (input(" A.) View balance\n B.) Withdraw\n C.) Deposit\n D.) View total withdraws\n E.) View total deposits\n F.) Quit\n"))
        if option_choice == 'a':
            print(user_one_bank.show_info())

        elif option_choice == 'b':
            print(user_one_bank.withdraws())
            
        elif option_choice == 'c':
            print(user_one_bank.deposit())
            
        elif option_choice == 'd':
            print(f"There have been {user_one_bank.total_withdraws} withdraws.\n\n\n")
            
        elif option_choice == 'e':
            print(f"There have been {user_one_bank.total_deposits} deposits.\n\n\n")
            
        elif option_choice == 'f':
            print("\t\tThank you for using The Money Bank.\n")
            return False
            break
        else:
            print("Please choose a letter from A to F.")


def bank_creation(name):
    balance = float(input(f"{name.name}, please enter a starting amount: "))
    return balance



while True:

    print("\n\n\t\tWelcome to The Money Bank!\n")
    name = input("Please enter your name: ")
    occupation = input("Next, enter your occupation: ")
    user_one = User(name, occupation)
    
    new_user = input("Would you like to sign up for a new account today? Type 'yes' to proceed or 'no' to cancel.\n")
    if new_user.lower() == 'yes':
        user_one_balance = bank_creation(user_one)
        user_one_bank = bank(user_one.name, user_one.occupation, user_one_balance)
        
        nextphase = options(user_one)
        if nextphase == False:
            break
    elif new_user.lower() == 'no':
        print("\nYour transaction was successfully cancelled. Thank you for using The Money Bank.\n")
        break
    else:
        print("Invalid selection!")
        break