import random

correct_number = random.randint(1, 20)

user_number = int(input("Guess a number between 1 and 20: "))

if user_number == correct_number:
    print("Correct guess.")
else:
    print("wrong guess. The correct number was:", correct_number)