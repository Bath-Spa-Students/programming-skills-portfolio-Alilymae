#Factorial !
#3! = 3*2*1 = 6
#recursion
#a function that calls within itself
def factorial(x):
    if x == 1 : #base condition
        return 1
    else: #formula
        return x * factorial (x - 1)
    
print (factorial (3))

#I watched a yt tutorial but i still dont understand