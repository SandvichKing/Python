# Rock Paper Scissors game
while True:
    # Tallies up the player and computer's score per game
    player_score = 0
    computer_score = 0
    ties = 0
    import random

# Player makes a choice
    print(f"""Welcome to Rock, Paper, Scissors!""")
    print(f"""Make your choice:
    Rock = 1
    Paper = 2
    Scissors = 3
    Choose wisely...""")
    player_choice = int(input("Rock, Paper, or Scissors: "))
    possible_actions = [1, 2, 3]
    if possible_actions == 1:
        possible_actions = 'ROCK'
    elif possible_actions == 2:
        possible_actions = 'PAPER'
    else: possible_actions = 'SCISSORS'

# Catch if player chooses option outside of list
    while int(player_choice) not in possible_actions:
        player_choice = input("Invalid Choice. Please ensure you're typing the correct number. ")

# Display Player and Computer choices
    print(f"""You chose:
""", player_choice)
    computer_choice = random.choice(possible_actions)
    possible_actions = [1, 2, 3]
    if possible_actions == 1:
        possible_actions = 'ROCK'
    elif possible_actions == 2:
        possible_actions = 'PAPER'
    else: possible_actions = 'SCISSORS'
    print(f"""Computer chose:
""", computer_choice)

# Game logic - I need to make this more efficient somehow
# Need to fix the Scissors option - Doesn't print out winning result, computer will always choose paper?
    while True:
        if player_choice == computer_choice:
            print(f"It's a tie!")
        elif player_choice == "Rock" and computer_choice == "Paper":
            print(f"Paper beats Rock, You Lose!")
            computer_score +=1
        elif player_choice == "Rock" and computer_choice == "Scissors":
            print(f"Rock beats Scissors, You Win!")
            player_score +=1
        elif player_choice == "Paper" and computer_choice == "Rock":
            print(f'Paper beats Rock, You Win!')
            player_score +=1
        elif player_choice == "Paper" and computer_choice == "Scissors":
            print(f'Scissors beats Paper, You Lose!')
            computer_score +=1
        elif player_choice == "Scissors" and computer_choice == "Rock":
            print(f'Rock beats Scissors, You Lose!')
            computer_score +=1
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