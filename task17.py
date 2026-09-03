# file handling in python

# 1. open a file
with open("hello.txt", "w") as f:
    f.write("Hello, Python!")

# 2. read a file
with open("hello.txt", "r") as f:
    print(f.read())

# 3. append to a file
with open ("hello.txt", "a") as f:
    f.write("\nHave a nice day.")    

# 4. read lines from a file
with open("hello.txt", "r") as f:
    lines=f.readlines()
    print(lines)    
  
# 5. antha file eatkanave irukkaaa endu check panna 
# importing os module- ithu external module  
import os
print(os.path.exists("hello.txt"))

# innoru model file check irukkaa endu check panna ithu use pannuvom
# IMPORTING PATHLIB MODULE- ITHU INTERNAL MODULE (BUILT IN MODULE)
from pathlib import Path

file=Path("student.txt")
if file.exists():
    print("File exists")
else:
    print("File does not exist")


# 6. word count in a file
def word_count(filepath):
    with open(filepath, "r") as file:
        text = file.read()
    
    words = text.split()
    return len(words)

print(word_count("hello.txt"))    

# file irukkaa endu check panrathu
if os.path.exists("hello.txt"):
    print("File exists")
else:
    print("File does not exist")

# upload a folder(folder create panna)
os.makedirs("uploads", exist_ok=True)

# ithu file create aagitu endu naan paaka thaan intha code kuduthu irukkan
print("uploads folder is ready")

# innoru murai folder create panna
Path("uploads").mkdir(exist_ok=True)

# json file create panna
# built in module json use pannuvom
import json

# array cretate panrom
students = [
    {"name": "Santhu", "age": 20},
    {"name": "Satha", "age": 23},
    {"name": "Pavi", "age": 21}
]

# json file la save panna-dump
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)  # students enbathu variable irukku, athu json file la save aagum

# json file la irunthu data read panna-load
with open("students.json", "r") as f:
    students = json.load(f)

print(students)


import csv

# students.csv file-a create panrom
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # Heading write panrom
    writer.writerow(["Name", "Age"])

    # Student details write panrom
    writer.writerow(["Santhu", 20])
    writer.writerow(["Satha", 23])
    writer.writerow(["Pavi", 21])


# image binary file-a read panna and copy panna
with open("photo.jpg", "rb") as f:
    data = f.read()

with open("copy.jpg", "wb") as f:
    f.write(data)

print("done")

