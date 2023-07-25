import random

x = int(input("How high of a number do you want to guess : "))
randomNumber = random.randint(0, x)
loops = 0
while(True):
    loops += 1
    guess = int(input("Enter your guess : "))
    if(guess > randomNumber):
        print("You are above the number")
    elif(guess < randomNumber):
        print("You are below the number")
    else:
        print(f"You have guessed the number {randomNumber} correctly in {loops} tries")
        break
        