a=int(input("enter the number:"))
for i in range(2,a-1):
    if a%i==0:
        print("is not a prime")
        break
else:
    print("is a prime")
