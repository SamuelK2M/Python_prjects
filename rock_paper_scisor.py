import random

#The game need to ask "RocK, Paper, or scisor
# 
# need to type"r/p/ss"
# 
# after chosing the computer need to ramdom its choice
# 
# need to enter rules of the game
# 
# and #  

emojis = {'r' : '🪨', 'p': '📄', 's': '✂️'}
choices = ('r','p','s')

while True:
    player_choice = input ('Rock, Paper, or scissors ? (R/P/S)').lower()
    if player_choice not in choices:
        print ('Invalid choice !')
        continue

    computer_choice = random.choice(choices)

    print(f'you chose {emojis[player_choice]}')
    print(f'computer chose {emojis [computer_choice]}')

    if player_choice == computer_choice:
        print('Tie ')
    elif (
        (player_choice == 'r' and computer_choice == 's') or
        (player_choice == 's' and computer_choice == 'p') or
        (player_choice == 'p' and computer_choice == 'r')):
        print('You win !')
    else:
        print('you loss !')

    continue_playing = input('play again ? (y/n):').lower()
    if continue_playing == 'n':
        print("Thanks for palying !")
        break