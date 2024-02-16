# Rock Paper Scissors game
while True:
    import random

# Player makes a choice
    possible_actions = ["Rock", "Paper", "Scissors"]
    print(f"Choose between rock, paper, scissors")
    player_choice = input("Rock, Paper, or Scissors: ")

# Catch if player chooses option outside of list
    while player_choice not in possible_actions:
        player_choice = input("Invalid Choice. Choose Rock, Paper, or Scissors: ")

# Display Player and Computer choices
    print(f"""You chose:
""", player_choice)
    computer_choice = random.choice(possible_actions)
    print(f"""Computer chose:
""", computer_choice)

# Game logic - I need to make this more efficient somehow
# Need to fix the Scissors option - Doesn't print out winning result, computer will always choose paper?
    while True:
        player_score = 0
        computer_score = 0
        if player_choice == computer_choice:
            print(f"It's a tie!")
        elif player_choice == "Rock" and computer_choice == "Paper":
            print(f"Paper beats Rock, You Lose!")
        elif player_choice == "Rock" and computer_choice == "Scissors":
            print(f"Rock beats Scissors, You Win!")
            player_score +=1
        elif player_choice == "Paper" and computer_choice == "Rock":
            print(f'Paper beats Rock, You Win!')
            player_score +=1
        elif player_choice == "Paper" and computer_choice == "Scissors":
            print(f'Scissors beats Paper, You Lose!')
        elif player_choice == "Scissors" and computer_choice == "Rock":
            print(f'Rock beats Scissors, You Lose!')
        elif player_choice == "Scissors" and computer_choice == "Paper":
            print(f'Scissors beats Paper, You Win!')
            player_score +=1
        break
    print("The Player's score is: ", player_score)
    print("The Computer's score is: ", computer_score)

# Ask player if they want to play again
    play_again = input('Do you want to play again[yes/no]? ')
    if play_again.lower() == 'no':
        print(f"Thanks for playing!")
        break