product_name=input("Enter your product name: ")
price=input("Enter your product price: ")
quantity=input("Enter your product quantity: ")

total_amount=int(price)*int(quantity)

if total_amount >= 5000:
    discount = total_amount * 10 / 100
    final_amount = total_amount - discount
else:
    final_amount = total_amount
    discount= 0

# printing the output
print("Product Name:", product_name)
print("Total Amount:", total_amount)
print("Discount:", discount)
print("Final Amount:", final_amount)