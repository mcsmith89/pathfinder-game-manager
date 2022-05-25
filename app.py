from player import Player, creatNewPlayer
from printy import printy, inputy

#___________________________
#Mock players DB 
players = []
#Seeding list to test update function
mike = Player("Mike", "Smith", "test@testemail.com")

players.append(mike)

mike.addWeapon("Longsword")
mike.addItem("Frogs Tears")
mike.updateBalance("gold", 500)

#_________________________________
#Testing printing and accepting options
userOptions = ["1. Create Player", "2. Update Player"]
print(f"What would you like to do?")
for x in userOptions:
    print(x)
beginningChoice = inputy("[n]Please select an option ", type="int")

if beginningChoice > len(userOptions):
    printy(f"[r]You chose {beginningChoice} which is not an option.")
else:
    printy(f"[n]You have chosen: {userOptions[beginningChoice-1]}")
    if beginningChoice == 1:
        players.append(creatNewPlayer())

for x in players:
    print(vars(x))

# confirmation = inputy("[r]Are you sure you want %s?" % ("Choice"), type="bool", options=["y", "n"], condition="i") #Keep as a reference for command line 
# name = inputy("[b]what player are you looking to impacty %s?" % ("Choice"), type="str") #Keep as a reference for command line 

# print(name)