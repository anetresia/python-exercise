students = ["Kamal", "Niro", "Arun"]
student1 = students
student2 = ["Kamal", "Niro", "Arun"]
search_name = "Niro"
missing_name = "Siva"
result = None
print(student1 is students)
print(student1 is student2)
print(student1 == student2)
print(search_name in students)
print(missing_name in students)
print(result is None)
print("Kamal" in student2)
