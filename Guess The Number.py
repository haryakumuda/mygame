from ast import IsNot
import random

print("Welcome to Guess The Number!")
print("pick a number from 1 to 100")


r = random.randint(1, 100)
r = 10
userinput = input("Type a number: ")

while True:
    if userinput.isdigit():
        userinput = int(userinput)
        if userinput < 1:
            print("Please type a number between 1 - 100!")
            userinput = input("Type a number: ")
        elif userinput > 100:
            print("Please type a number between 1 - 100!")
            userinput = input("Type a number: ")
        else:
            if userinput > r:
                print("You were above the number!")
                break
            elif userinput < r:
                print("You were below the number!")
                break
            else:
                print("AMAZING!")
                break
    else:
        print("Please type between 1 - 100!")
        userinput = input("Type a number: ")

guess = 1
while userinput != r:
    guess += 1
    userguess = input("Make a guess: ")
    if userguess.isdigit():
        userguess = int(userguess)
    else:
        print("Please type a number!")
        continue
    
    if userguess == r:
        print("WOW YOU GOT IT!")
        break
    elif userguess > r:
         print("You were above the number!")
    else:
         print("You were below the number!")
print("You got it in", guess, "Guess(s)")
print("Congratulations!")