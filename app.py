from player import Player

def creatNewPlayer():
    None
    #Add input output logic here then create the player

#Just testing it worked 
mike = Player("Mike", "Smith", "test@testemail.com")
mike.addWeapon("Longsword")
mike.addItem("Frogs Tears")
mike.updateBalance("gold", 500)

print(vars(mike))
