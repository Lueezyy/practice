import random

def battle(choice, botChoice):
    if choice == botChoice:
        print(f"It is a draw! You both picked {choices[choice]}!")
    elif choice > botChoice:
        if choice - botChoice > 1:
            print(f"The bot wins! {choices[botChoice].title()} beats {choices[choice]}!")
        else:
            print(f"You win! {choices[choice].title()} beats {choices[botChoice]}!")
    else:
        if botChoice - choice > 1:
            print(f"You win! {choices[choice].title()} beats {choices[botChoice]}!")
        else:
            print(f"The bot wins! {choices[botChoice].title()} beats {choices[choice]}!")

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