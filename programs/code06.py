import random

def battle(choice, botChoice):
    if choice == botChoice:
        print("It is a draw!")
    elif choice > botChoice:
        if choice - botChoice > 1:
            print("The bot wins!")
        else:
            print("You win!")
    else:
        if botChoice - choice > 1:
            print("You win!")
        else:
            print("The bot wins!")

choices = ["rock", "paper", "scissors"]
print("Let's play rock paper scissors!")

while True:
    try:
        choice = input("\nEnter your choice (rock, paper, scissors, or q to quit): ").lower().strip()
        if choice == "q":
            break
        choice = choices.index(choice.lower().strip())
        botChoice = random.randint(0, 2)
        print(f"The bot chose {choices[botChoice]}")
        battle(choice, botChoice)
    except:
        print("\nError: Please enter either rock, paper, or scissors.")