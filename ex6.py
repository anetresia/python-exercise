num1=input("Enter a number: ")
num2=input("Enter another number: ")
operator=input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = float(num1) + float(num2)
    print("The result is:", result)
elif operator == "-":
    result = float(num1) - float(num2)
    print("The result is:", result)
elif operator == "*":
    result = float(num1) * float(num2)
    print("The result is:", result)
elif operator == "/":
    result = float(num1) / float(num2)
    print("The result is:", result)