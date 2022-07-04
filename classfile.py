# Parent class
class User:
    
    Transaction_type = 'Moneymarket'   # Attribute ---->> is a better way to add a user type to each class
    add_funds = 100
    
    # Constructor/Initializer of object
    def __init__(self, name, funds): # __init__ is a keyword to initialize an object "self" is an object
        self.name = name            # can do your own __init__ for each child class
        self.funds = funds
        self.type = 'CD'    



# Child class of User

class Debit(User):
    Transaction_type = 'Deposit'
    #add_funds = 100

    #def __init__(self, name, funds):       
        #super().__init__(name, funds)
  


