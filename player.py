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
    None
    #Add input output logic here then create the player add the other functions here 
    #Include the actual options below then move the functions to their own file 
