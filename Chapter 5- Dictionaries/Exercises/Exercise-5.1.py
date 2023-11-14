#creating a dictionary of a person's profile
person = {
    "First name" : "Satoru" ,
    "Last name" : "Gojo" ,
    "Age" : 28 ,
    "City" : "Tokyo"
}

#printing each of the info from the dictionary
for key, value in person.items():
    print (f"{key}: {value}")