import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print('Welcome to City, Country, River! Have fun! :)')

response = input('Would you like to read the game rules? (y/n) ')
game_rules = ('You have 30 seconds to fill in the blanks. Each correct answer scores 1 point. The points are added up after each round; the person with the most points wins.')

if response.lower() == 'y':
    print(f'Here are the game rules: {game_rules}')
elif response.lower() == 'n':
    print('Okay, we will skip the game rules. Have fun playing :)')
else:
    print("Invalid input, please enter 'y' for Yes or 'n' for No.")

question_rounds = input('How many rounds do you want to play? (1-5) ')

try:
    question_rounds = int(question_rounds)
except ValueError:
    print("Invalid number of rounds. Setting to default of 1 round.")
    question_rounds = 1

start_game = input('Press "s" to start the game ')

if start_game.lower() == 's':
    for round in range(question_rounds):
        random_letter = random.choice(letters)
        print(f'Round {round + 1}: The letter is {random_letter}')
        
        city = input('City? ')
        country = input('Country? ')
        river = input('River? ')
        
else:
    print("Game not started. Please press 's' to start the game.")
