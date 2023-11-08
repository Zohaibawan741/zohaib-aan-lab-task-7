import random

choices = ["rock", "paper", "scissors"]
user_choice = input("Rock, Paper, or Scissors? ").strip().lower()
computer_choice = random.choice(choices)

if user_choice in choices:
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")