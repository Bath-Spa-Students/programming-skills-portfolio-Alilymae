#bigger amount
am_1  = 11
am_2 = 99

#headache
if am_1 > 10:
    if am_2 < 100:
        if am_1 > am_2:
            print (f"{am_1} is greater.")
        elif am_1 < am_2:
            print (f"{am_2} is greater")
        else: 
            print ("Theyre the same")
    else:
        print ("am_2 is not greater than 100")
else:
    print ("am_1 is not greater than 10") 


