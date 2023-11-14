#movie tickets pricing
print ("Movie ticket prices may vary for different ages")

#using a while loop to repeat the code
while True:
    m_tickets = (input("State your age: "))
    tickets = (int(m_tickets))

     #if the person is below 3, tickets are free
    if tickets < 3:
        print ("The ticket is free!")

     #if the person is >3 or < 12, tickets are $10
    elif 3 <= tickets <= 12:
        print ("The ticket cost $10 per person")

    #if the persons age is >12, tickets are $15
    else:
        print ("The tickets cost $15 per person")
    break
print ("Thank you for your purchase!")