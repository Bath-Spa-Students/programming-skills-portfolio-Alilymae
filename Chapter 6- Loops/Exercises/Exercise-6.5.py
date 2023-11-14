#Copy of code from exerise-6.4 
#list of sandwiches w/ pastrami x3
sandwiches = ["Chicken Sandwich", "Grilled Cheese Sandwich", 
              "Vegan Sandwich", "Tuna Sandwich", "Nutella Sandwich",
                "Pastrami", "Pastrami", "Pastrami"]
f_s = [] #empty list
print ("I'm sorry but we've run out of Pastrami Sandwiches\n")

#looping through the sandwich orders and removing pastrami
while "Pastrami" in sandwiches:
    sandwiches.remove("Pastrami") #remove Pastrami

while sandwiches:
    order = sandwiches.pop(0) #removing them from the list 1b1 since order is done
    print (f"Your order of a {order} is ready!")
    f_s.append(order) #adding orders finished to f_s

print ("\nOrders pushed out:") 
#looping n printing the orders that are finished
for s in f_s:
    print (s)
