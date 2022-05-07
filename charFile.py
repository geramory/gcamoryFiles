
# Parent class
class User:
    
    Transaction_type = 'CD'   # Attribute ---->> is a better way to add a animal type to each class
    add_funds = 100
    # Constructor/Initializer of object
    def __init__(self, name, funds): # __init__ is a keyword to initialize an object "magic method" "self" is an object
        self.name = name            # can do your own __init__ for each child class
        self.funds = funds
        self.type = 'CD'    # Students' way to add type of animal in constructor, overriding constructor



# Child class of User

class Debit(User):
    Transaction_type = 'Deposit'
    #add_funds = 100

    #def __init__(self, name, funds):       
        #super().__init__(name, funds)
  


class Money(User):
    Tansaction_type = 'Moneymarket'

#if __name__=='__main__':  # __name__  the behavior of how we run our module
#main()













