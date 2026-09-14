# exception(error handling)
# 1
try:
    x=10
    y=0
    print(x/y)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 2
try:
    x=int("hello")
except ValueError:
    print("Error: Invalid value for conversion to integer.")

# 3.
try:
    x = 10
    y = 2
    print(x / y)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

finally:
    print("Done")

# 4.
try:
    number = -5

    if number < 0:
        raise ValueError("Number cannot be negative.")

    print(number)

except ValueError as e:
    print("Error:", e)

# 5.
try:
    with open("index.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("Error: File not found.")