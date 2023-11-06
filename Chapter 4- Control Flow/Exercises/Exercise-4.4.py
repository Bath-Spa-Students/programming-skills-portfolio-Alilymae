#Stages of life
player = (input("What is your name: "))
age = (int(input("What is your age: ")))

#and so starts the complicated part... >:(
#if your below 2, your a baby
if age <= 2 :
    print (f"{player} is a baby")

#If your at least 2 and below 4, your a small child
elif age >= 2 and age < 4:
    print (f"{player} is a toddler")

#If your at least 4 and below 13, your a child    
elif age >= 4 and age < 13:
    print (f"{player} is a kid")

#If your at least 20 and below 65, your of legal age
elif age >= 20 and age < 65:
    print (f"{player} is an adult")

#If your at 65 and above, your a senior citizen.
elif age >= 65:
    print (f"{player} is an senior citizen")

#printing my title at the end.
else:
    print (str("stages of life..."))