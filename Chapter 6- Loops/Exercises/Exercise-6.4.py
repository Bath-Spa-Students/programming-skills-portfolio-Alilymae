#list of sandwiches
sandwiches = ["Chicken Sandwich", "Grilled Cheese Sandwich", "Vegan Sandwich", "Tuna Sandwich", "Nutella Sandwich"]
f_s = [] #empty list

#looping through the sandwich orders
while sandwiches:
    order = sandwiches.pop(0) #removing them from the list 1b1 since order is done
    print (f"Your order of a {order} is ready!")
    f_s.append(order) #adding orders finished to f_s

print ("\nOrders pushed out:") 
#looping n printing the orders that are finished
for s in f_s:
    print (s)
