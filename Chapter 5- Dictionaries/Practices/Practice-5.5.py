#merging dictionaries 
#reuse, reduce, recycle
me_myself_and_I = {
    "Name" : "Aliah Mae",
    "Age" : 17,
    "Height" : "163cm",
    "Fav_color" : "Red",
    "Nationality" : "Filipino",
    }
me_again = {
    "Birthdate" : "July 20 2006",
    "Status" : "Broke",
    "Mental status" : "Highly unstable",
    "Motto" : "Delulu is the Solulu"
}
me_again.copy() #had to google how to use copy
me_myself_and_I.update(me_again)
print (me_myself_and_I)
