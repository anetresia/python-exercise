password=input("Enter your password: ")

has_length=len(password) >= 8
has_upper=False
has_lower=False

for char in password:
    if char.isupper():
        has_upper=True  
    elif char.islower():
        has_lower=True



if has_length and has_upper and has_lower:
    print("Strong Password.")
else:
    print("Weak Password.")