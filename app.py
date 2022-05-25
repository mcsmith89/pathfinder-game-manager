from player import Player, creatNewPlayer
from printy import printy, inputy


#Just testing it worked 
mike = Player("Mike", "Smith", "test@testemail.com")
mike.addWeapon("Longsword")
mike.addItem("Frogs Tears")
mike.updateBalance("gold", 500)

print(vars(mike))

#Testing printing and accepting options
userOptions = ["1. Create Player", "2. Update Player"]
print(f"What would you like to do?")
for x in userOptions: 
    print(x)
beginningChoice = inputy("[g]Please select an option ", type="int")

if beginningChoice > len(userOptions):
    printy(f"[r]You chose {beginningChoice} which is not an option.")
else:
    printy(f"[n]You have chosen: {userOptions[beginningChoice-1]}")

# confirmation = inputy("[r]Are you sure you want %s?" % ("Choice"), type="bool", options=["y", "n"], condition="i") #Keep as a reference for command line 
# name = inputy("[b]what player are you looking to impacty %s?" % ("Choice"), type="str") #Keep as a reference for command line 

# print(name)