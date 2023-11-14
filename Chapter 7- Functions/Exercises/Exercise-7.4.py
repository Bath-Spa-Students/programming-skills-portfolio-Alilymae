#using func for shirt size and message with fixed size
def shirt(size = "Large", text = "I Love Python"):
    print (f"Your shirt size is {size}\nMessage: {text}\n")


#L shirt and deafult message
shirt()
#M shirt and default message
shirt(size = "Medium")
#any size but diff. text.
shirt(size = "Small", text = "Good morning Starshine! The earth says HELLO!")