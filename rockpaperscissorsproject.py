import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nuser chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both user and computer selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! user win!")
        else:
            print("Paper covers rock! user lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! user win!")
        else:
            print("Scissors cuts paper! user lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! user win!")
        else:
            print("Rock smashes scissors! user lose.")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thank you for playing")
        break
    
    

