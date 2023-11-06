#Double decision
human = (input("What do you want to eat? Spaghetti or Carbonara: "))
food = human
if food.upper() == "SPAGHETTI":
     print ("Eat the Spaghetti!")
else :  
    print ("Eat the Carbonara!")

#Single Decision
human = (input("Are you hungry?: "))
while True:
    if "yes":
        print ("Go eat!")
    break