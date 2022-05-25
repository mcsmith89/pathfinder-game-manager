from printy import printy, inputy

#create the player and associated details 

class Player():
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.balance = {"gold":float(0), "silver":float(0)}
        self.weapons = {}
        self.items = {}

    def updateBalance(self, type, amount): 
        self.balance[type] += (amount)
        print(f"{self.first_name}'s balance is now {self.balance}")

    def addWeapon(self, weapon):
        self.weapons.update({weapon:{}})
    
    def addItem(self, item):
        self.items.update({item:{}})

def creatNewPlayer():
    first_name = inputy("[n]What is your first name? ", type="str")
    last_name = inputy("[n]What is your last name? ", type="str")
    email = inputy("[n]What is your email? ", type="str")

    globals()[(str(first_name[0])+str(last_name))] = Player(first_name=first_name, last_name=last_name, email=email) #This is how you use an output from a variable as the name for another

    print(vars(globals()[(str(first_name[0])+str(last_name))]))
    return globals()[(str(first_name[0])+str(last_name))]

def updatePlayer():
    None    

    # str(first_name[0]) + str(last_name) = Player(first_name=first_name, last_name=last_name, email=email) #how do we pass this? <<<-------

    #Add input output logic here then create the player add the other functions here 
    #Include the actual options below then move the functions to their own file