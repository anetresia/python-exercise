# question 1
name=str(input("Enter your name: "))

marks1=int(input("Enter your marks for subject 1 marks: "))
marks2=int(input("Enter your marks for subject 2 marks: "))
marks3=int(input("Enter your marks for subject 3 marks: "))

total=marks1 + marks2 + marks3
average=total/3

if average>=75:
    grade="A"
elif average>=60:
    grade="B"
elif average>=40:
    grade="C"
else:
    grade="fail"

# ithu thaniya output mattum varum
print(name)
print(total)
print(average)   
print(grade)

# ithu output oda munnnukku naanka kudukurathum varum
print(" Student Name:", name)
print(" Total Marks:", total)
print(" Average Marks:", average)
print(" Grade:", grade)
