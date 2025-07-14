'''secret_number = 7
guess_from = 0
guess_times = 3

while guess_from < guess_times:
    guess = int(input("Guess a number (1-10)"))
    guess_from += 1

    if guess > secret_number:
        print("Lower!")
        print(f"{guess_times - guess_from} trials remaining!")
    elif guess < secret_number:
        print("Higher!")
        print(f"{guess_times - guess_from} trials remaining!")

    else:
        print("Hurray! You guessed correctly")
        break

else:
    print("You Failed the correct number was 7")'''

secret_number = 4823
start_from =0
trials = 3

while start_from < trials:
    guess=int(input("Enter a number! "))
    start_from += 1
    if guess == secret_number:
        print("Hurray! Guessed correctly!")
        break
    elif guess > secret_number:
        print("Lower")
        print(f"{trials - start_from} trial(s) remaining!")
    else:
        print("Higher")
        print(f"{trials - start_from} trial(s) remaining!")
        if trials - start_from == 0:
            print("Sim Card Locked")

'''
else:
    print("Poor you! You failed")'''