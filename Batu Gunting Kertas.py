import random
user_wins = 0
computer_wins = 0
option = ['rock', 'paper', 'scissors']
def score():
        print(user_name + ":", user_wins, "wins")
        print("Computer:", computer_wins, "wins")

user_name = input("Write your name: ")

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in option:
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = option[random_number]
    print("Computer picked", computer_pick)

    if user_input == 'rock' and computer_pick == 'scissors':
        print("You Win!")
        user_wins += 1
        score()
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You Win!")
        user_wins += 1
        score()
    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You Win!")
        user_wins += 1
        score()
    elif user_input == 'rock' and computer_pick == 'rock':
        print("It's A Tie")
        score()
    elif user_input == 'paper' and computer_pick == 'paper':
        print("It's A Tie")
        score()
    elif user_input == 'scissors' and computer_pick == 'scissors':
        print("It's A Tie")
        score()
    else:
        print("You Lose!")
        computer_wins += 1
        score()


score()
print("Goodbye!")
