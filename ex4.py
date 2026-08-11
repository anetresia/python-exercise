username=input("Enter your username: ")

# start and endla unwanted space remove pannum
username=username.strip()
# small letters aa change pannum
username=username.lower()
# onda innondaa maathum
username=username.replace(" ","_")

print("formatted username:", username)