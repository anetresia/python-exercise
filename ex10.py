store_username=str("resia@gmail.com")
store_password=str("resia_2406")
username=input("Enter your username: ")
password=input("Enter your password: ")

if username == store_username and password == store_password:
    print("Login successful.")
else:
    print("Invalid username or password.")

print("Data type of username:", type(username))
print("Data type of password:", type(password))