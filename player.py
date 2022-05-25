#create the player and associated details 
from graphql import SchemaMetaFieldDef


class Player():
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.balance = float(0) 
        self.weapons = {}

    def updateBalance(self, amount): 
        self.balance += (amount)
        print(f"{self.first_name}'s balance is now {self.balance}")

    def addWeapon(self, weapon):
        self.weapons.update({weapon:{}})
