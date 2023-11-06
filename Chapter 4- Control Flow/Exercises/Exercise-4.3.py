#alien colors pt. 3
ques = (input("What color is your Alien: "))
alien1 = ques

#idk why I even bothered usinga while loop here
#If alien is green it says you get 5 points.
while True:
    if alien1.casefold() == "green":
        print ("Yay! You just got 5 points")
        break
#If alien is yellow it says you get 10 points.
    elif alien1.casefold() == "yellow":
        print ("Yay! You just got 10 points")
        break
#If alien is red it says you get 15 points.
    elif alien1.casefold() == "red":
        print ("Yay! you just got 15 points")
        break
#too bad you didnt get any of the 3 color alien :(
    else : 
        print ("What color is your alien: red, yellow, or green.")
        break