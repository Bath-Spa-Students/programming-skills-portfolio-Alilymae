#Shrinking the list
names = ["Itadori", "Megumi", "Nobara", "Gojo", "Nanami"]
print (f"Hello! Welcome to Jujutsu Restaurant {names[0]} How may I help you?")
print (f"Hello! Welcome to Jujutsu Restaurant {names[1]} How may I help you?")
print (f"Hello! Welcome to Jujutsu Restaurant {names[2]} How may I help you?")
print (f"Hello! Welcome to Jujutsu Restaurant {names[3]} How may I help you?")
print (f"Hello! Welcome to Jujutsu Restaurant {names[4]} How may I help you?")
#Changing Nanami to Geto
print (f"It seems {names[4]} is busy so we'll give his seat to our new friend")
names [4] = "Geto"
print (f"Hello! Welcome to Jujutsu Restaurant {names[0]} How may I help you?")
print (f"Hello! Welcome to Jujutsu Restaurant {names[1]} How may I help you?")
print (f"Hello! Welcome to Jujutsu Restaurant {names[2]} How may I help you?")
print (f"Hello! Welcome to Jujutsu Restaurant {names[3]} How may I help you?")
print (f"Hello! Welcome to Jujutsu Restaurant {names[4]} How may I help you?")
#There are only 2 tables so remove the rest
print ("Oh no! It's seems that we can't invite everyone to dinner, there are only 2 seats available...")
#Deleting the other's name using pop
print (f"I'm sorry {names[0]}, you cant join us for today")
names.pop(0)
print (f"I'm sorry {names[0]}, you cant join us for today")
names.pop(0)
print (f"I'm sorry {names[0]}, you cant join us for today")
names.pop(0)
print (f"To the two of you, {names[0]} and {names[1]} you are still invited and we have a table for you both")

#Emptying the list
del names[0:2]
print (names)