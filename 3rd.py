a=(input("enter the gender:"))
b=int(input("enter the age:"))
c=int(input("enter the annual income:"))
if a=="female" and b>=60 and c<=200000:
    print("you are eligible for pension")
    print("Thank you for your service")
else:
    print("you are not eligible for pension")