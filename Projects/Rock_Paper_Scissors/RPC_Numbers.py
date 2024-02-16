# Rock paper Scissors game but with numbers instead of strings
# Greet the player and give instructions
print(f"Welcome to rock paper scissors but using numbers instead of string values")
print(f"""Make your choice of:
      ROCK = 1
      PAPER = 2
      SCISSORS = 3""")
# Get Player Choice
player_choice = int(input("Enter 1, 2, or 3: "))
def get_player_choice():
    if player_choice == 1:
        player_choice = 'ROCK'
    elif player_choice == 2:
        player_choice = 'PAPER'
    else:
        player_choice = 'PAPER'
    return get_player_choice
print("The Player chose: ", player_choice)



# Get Computer choice
#def get_computer_choice():
 #   import random
    

# Determine the winner
#def determine_winner():

# Play again?
#def play_again():