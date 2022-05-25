from player import Player
from printy import printy, inputy

def creatNewPlayer():
    None
    #Add input output logic here then create the player

#Just testing it worked 
mike = Player("Mike", "Smith", "test@testemail.com")
mike.addWeapon("Longsword")
mike.addItem("Frogs Tears")
mike.updateBalance("gold", 500)

print(vars(mike))

print("What would you like to do? \n1. Create Player\n2. View Players \n3. Update Player")
userChoice = inputy("[g]Please select an option ", type="int")

print(f"You have chosen {userChoice}")

# confirmation = inputy("[r]Are you sure you want %s?" % ("Choice"), type="bool", options=["y", "n"], condition="i") #Keep as a reference for command line 
# name = inputy("[b]what player are you looking to impacty %s?" % ("Choice"), type="str") #Keep as a reference for command line 

# print(name)