'''i = 1
while i<=5:
    print (i)
    i = i + 1

print("Gone")'''

'''i = 3
while i <= 10:
    print('*' * i)
    i = i + 1

print ("Done")'''

'''name = input("Enter your name ")

while name == "":
    print("You did not enter anything")
    name = input("Enter your name ")
else:
    print(f"Hello {name}")'''

'''i = 1

while i <= 6:
    print('r' * i)
    i += 1'''

'''age = int(input("Enter your age: "))

while age <= 0:
    print("Your age can't be a non-positive number")
    age = int(input("Enter your age: "))
else:
    print(f"Hey you are {age} years old'''

'''food = input("Enter food you like (q to quit)")

while  food != 'q':
    print(f"You like {food}.")
    food = input("Enter another food you like (q to quit)")

print("You eat alot")'''

'''num = int(input("Enter a num 1 -10:"))

while num <= 0 or num > 10:
    print("Read instructions!!")
    num = int(input("Enter a num 1 -10"))

print(f"You chose {num}")'''

'''command = input("")

if command == 'help':
    print("Start --> Start the car")
    print("Stop --> Stop the car")
    print("quit --> quit the game")

while command == 'start':
    print("Car started!")
    command = input("")
    while command == 'stop':
        print("Car stopped!") 
        command = input("")
        while command == 'quit':
            print("Bye")
            break
else:
    print("Not recognised as an internal or external command")'''

'''command = input("")

while command == 'help':
    print("Start --> Start the car")
    print("Stop --> Stop the car")
    print("quit --> quit the game")
    command = input("")
    while command == 'start':
        print("Car started!")
        command = input("")
        while command == 'stop':
            print("Car stopped!") 
            command = input("")
            while command == 'quit':
                break





print("Not recognised as an internal or external command")'''

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started")
    elif command == 'stop':
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car stop")
    elif command == 'help':
        print("Start --> Start the car")
        print("Stop --> Stop the car")
        print("quit --> quit the game")
    elif command == 'quit':
        break
    else:
        print("Not recognised as an internal or external command")




