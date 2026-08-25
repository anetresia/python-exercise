# ex 1
employees = [
    {"name": "Pavi", "department": "IT", "salary": 120000},
    {"name": "Satha", "department": "HR", "salary": 85000},
    {"name": "Santhu", "department": "Finance", "salary": 110000},
    {"name": "Resia", "department": "IT", "salary": 95000}
]


def analyze_employees(employees):

    total = 0
    highest = 0
    highest_name = ""

    IT = 0
    HR = 0
    Finance = 0

    for employee in employees:

        total = total + employee["salary"]

        if employee["salary"] > highest:
            highest = employee["salary"]
            highest_name = employee["name"]

        if employee["department"] == "IT":
            IT = IT + 1
        elif employee["department"] == "HR":
            HR = HR + 1
        elif employee["department"] == "Finance":
            Finance = Finance + 1

        if employee["salary"] > 100000:
            print("Salary above 100000:", employee["name"])

    print("Total Salary:", total)
    print("Highest Salary:", highest)
    print("Highest Salary Employee:", highest_name)
    print("IT Employees:", IT)
    print("HR Employees:", HR)
    print("Finance Employees:", Finance)


analyze_employees(employees)



# ex 2
products = {
    "Laptop": {"price": 120000, "quantity": 5},
    "Phone": {"price": 80000, "quantity": 15},
    "Keyboard": {"price": 5000, "quantity": 0},
    "Mouse": {"price": 3000, "quantity": 7}
}


def calculate_inventory(products):

    total = 0
    expensive = ""
    highest_price = 0

    for product in products:

        price = products[product]["price"]
        quantity = products[product]["quantity"]

        total = total + (price * quantity)

        if quantity == 0:
            print("Out of stock:", product)

        if price > highest_price:
            highest_price = price
            expensive = product

        if quantity < 10:
            print("Quantity below 10:", product)

    print("Total Inventory Value:", total)
    print("Most Expensive Product:", expensive)
    print("Highest Price:", highest_price)


calculate_inventory(products)



# ex 3
sentence = input("Enter a sentence: ")

words = sentence.lower().split()

word_count = {}
highest_word = ""
highest_count = 0

for word in words:

    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

    if word_count[word] > highest_count:
        highest_count = word_count[word]
        highest_word = word

print("Word Count:", word_count)
print("Most Frequent Word:", highest_word)
print("Frequency:", highest_count)



# ex 4
cart = [
    {"name": "Laptop", "price": 120000, "quantity": 1},
    {"name": "Mouse", "price": 3000, "quantity": 2},
    {"name": "Keyboard", "price": 5000, "quantity": 1}
]


def calculate_bill(cart):

    total = 0
    expensive_item = ""
    highest_cost = 0

    for item in cart:

        subtotal = item["price"] * item["quantity"]

        print(item["name"], "Subtotal:", subtotal)

        total = total + subtotal

        if subtotal > highest_cost:
            highest_cost = subtotal
            expensive_item = item["name"]

    print("Total Bill:", total)

    if total > 100000:
        discount = total * 10 / 100
        total = total - discount

        print("Discount:", discount)

    print("Final Bill:", total)
    print("Most Expensive Item:", expensive_item)


calculate_bill(cart)



# ex 5 (naan explain pannanum)
books = [
    {"title": "Python Basics", "author": "John", "category": "Programming", "available": True},
    {"title": "Harry Potter", "author": "J.K. Rowling", "category": "Fiction", "available": False},
    {"title": "JavaScript Guide", "author": "John", "category": "Programming", "available": True},
    {"title": "The Alchemist", "author": "Paulo Coelho", "category": "Fiction", "available": False}
]


def library_info(books):

    programming = 0
    fiction = 0
    borrowed = 0

    author_name = input("Enter author name: ")

    for book in books:

        # Available books
        if book["available"] == True:
            print("Available Book:", book["title"])

        # Category count
        if book["category"] == "Programming":
            programming = programming + 1

        elif book["category"] == "Fiction":
            fiction = fiction + 1

        # Books by particular author
        if book["author"] == author_name:
            print("Book by", author_name, ":", book["title"])

        # Borrowed books
        if book["available"] == False:
            borrowed = borrowed + 1

    print("Programming Books:", programming)
    print("Fiction Books:", fiction)
    print("Borrowed Books:", borrowed)


library_info(books)



# ex 6
sales = {
    "January": 450000,
    "February": 520000,
    "March": 480000,
    "April": 600000,
    "May": 550000,
    "June": 490000
}


def analyze_sales(sales):

    total = 0
    highest = 0
    highest_month = ""
    lowest = 999999999
    lowest_month = ""
    above_500000 = 0

    for month in sales:

        amount = sales[month]

        total = total + amount

        if amount > highest:
            highest = amount
            highest_month = month

        if amount < lowest:
            lowest = amount
            lowest_month = month

        if amount > 500000:
            above_500000 = above_500000 + 1

    average = total / len(sales)

    print("Total Annual Sales:", total)
    print("Average Monthly Sales:", average)
    print("Highest Sales Month:", highest_month)
    print("Highest Sales:", highest)
    print("Lowest Sales Month:", lowest_month)
    print("Lowest Sales:", lowest)
    print("Months Above 500,000:", above_500000)


analyze_sales(sales)



# ex 7
students = ["John", "Sara", "John", "David", "Sara", "Anna"]


def remove_duplicates(students):

    unique_students = []
    seen = set()

    for student in students:

        if student not in seen:
            unique_students.append(student)
            seen.add(student)

    return unique_students


result = remove_duplicates(students)

print("Students:", result)