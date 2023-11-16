#season using elif statements
#UAE has only 3 seasons tho. hot, hotter, and hottest >:(
month = (input("Enter the month: "))

#case sens cus python is choosy
#use a while loop cus y not
while True:
    if month.lower() in ["november", "december", "january", "febraury"]:
        print ("Yay! It is Winter!") 
    elif month.lower() in ["march", "april", "may"]:
        print ("It's hot but its Spring!")
    elif month.lower() in ["june", "july","august"]:
        print ("It's very hot, It's Summer!")
    elif month.lower() in ["september", "october"]:
        print ("It's hot but its Autumn!")
    else:
        print ("Enter a month!")
    break


