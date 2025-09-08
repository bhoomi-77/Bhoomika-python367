age = int(input("enter the age"))
if age < 18 and age > 0:
    print("You are less than 18")
elif age == 0:
    print("age could not be less than 0")
else:
    print("you are above 18")