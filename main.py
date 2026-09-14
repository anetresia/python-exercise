# method 1
from greet import say_hello
say_hello("Resia")

# method 2
import greet
greet.say_hello("Resia")

# modules la 6th
from product import calculate_product_price
from discount import calculate_discount

price = calculate_product_price(1000, 2)

discount = calculate_discount(price)

final_price = price - discount

print("Final Price:", final_price)


# modules la 7th
import calculator

print(calculator.add(20, 10))
print(calculator.subtract(40, 20))