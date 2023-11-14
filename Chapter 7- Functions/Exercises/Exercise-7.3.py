#using func for shirt size and message
def shirt(size, text):
    print (f"Your shirt size is {size}\nMessage: {text}\n")


#positional arguments : arguments that needs to ne in proper order.
#Medium is the argument for size.
shirt("Medium", "I got a jar of dirt!!")

#Keyword arguments : uses keywords to identify the parameter.
shirt(size = "Medium", text = "I got a jar of dirt!!")