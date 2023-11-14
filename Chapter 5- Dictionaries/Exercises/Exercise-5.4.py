#rivers in the world using dictionaries
world_rivers= {
    "Niger" : "Nigeria",
    "Yangtze" : "China",
    "Yenisei" : "Russia"
}

#using a loop to write a sentence about each river
print ("3 rivers that run through countries:")
for r, c in world_rivers.items():
    print (f"The {r} river runs through {c}.")

#using a loop to print the name of each river in the dictionary
print ("List of rivers:")
for river in world_rivers.values():
    print (river)

#using a loopt to print the name of each country in the dictionary
print ("List of countries:")
for country in world_rivers.keys(): 
    print (country)