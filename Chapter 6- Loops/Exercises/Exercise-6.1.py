#Adding toppings to a empty crusty pizza
pizza = "You now have an empty pizza crust"
print(pizza)

while True:
    p = input("Add toppings: ") #add as much as u want

    if p.upper() == "QUIT": #if u wanna stop
        print("You stopped adding toppings")
        break
    else:
        print(f"You added {p}") #keep adding toppings
