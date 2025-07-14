sign = input("Is your weight in KG/LBS?")

if sign.upper() == 'KG':
    mass = float(input("Whats your weight in KG? ")) 

    lbs = mass * .45

    print(f"You are {lbs:.2f} Pounds")

elif sign.upper() == 'LBS':
    lbs = float(input("Whats your mass in pounds? "))
    mass = lbs / .45
    print(f"You are {mass:.2f} Pounds")

else:
    print("Enter a valid input(KG/LBS)")