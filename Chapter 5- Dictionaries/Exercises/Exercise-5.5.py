#different dictionaries for different pets
meow = {"Kind" : "Cat","Breed" : "Ragdoll", "Owner": "Suguru"}
woof = {"Kind" : "Dog", "Breed" : "Beagle", "Owner" : "John Wick"}
squeak = {"Kind" : "Rabbit", "Breed" : "Netherland dwarf", "Owner" : "Jaekyung"}
roar = {"Kind" : "Tiger", "Breed" : "White Tiger", "Owner" : "Nakyum"}

#storing it in a list.
pets = [meow, woof, squeak, roar]

#looping and printing 
for p in pets:
    print (f"Pet:\n {p['Kind']}")
    print (f"Breed:\n {p['Breed']}")
    print (f"Owner:\n {p['Owner']}")