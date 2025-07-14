name = input("Enter your name. ")

if len(name)> 10:
    print("Name cant exceed 10 characters")

elif len(name)<= 3:
    print("Name cant be less than 3 characters")

else:
    print("Name looks good!!")