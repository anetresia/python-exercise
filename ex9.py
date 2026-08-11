name=input("Enter your name: ")
tickets=input("Enter the number of tickets: ")
ticket_price=input("Enter the price: ")

total_cost=int(tickets)*int(ticket_price)

if int(tickets)>=5:
    discount = total_cost * 20/100
else:
    discount = 0


final_payment=total_cost-discount

print("customer name:", name)
print("Number of tickets:", tickets)
print("total amount:", total_cost)
print("Discount applied:", discount)
print("your final payment: ", final_payment)