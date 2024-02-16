# Rock Paper Scissors game
import random

possible_actions = ["Rock", "Paper", "Scissors"]
print(f"Choose between rock, paper, scissors")
player_choice = input("Rock, Paper, or Scissors: ")
print(f"You chose:", player_choice)
computer_choice = random.choice(possible_actions)
print(f"Computer chose:", computer_choice)

if player_choice == computer_choice:
    print(f"It's a tie!")
elif player_choice == "Rock" and computer_choice == "Paper":
    print(f"Paper beats Rock, You Lose!")
elif player_choice == "Rock" and computer_choice == "Scissors":
    print(f"Rock beats Scissors, You Win!")
elif player_choice == "Paper" and computer_choice == "Rock":
    print(f'Paper beats Rock, You Win!')
elif player_choice == "Paper" and computer_choice == "Scissors":
    print(f'Scissors beats Paper, You Lose!')
elif player_choice == "Scissor" and computer_choice == "Rock":
    print(f'Rock beats Scissors, You Lose!')
elif player_choice == "Scissor" and computer_choice == "Paper":
    print(f'Scissors beats Paper, You Win!')
