import random

# The rolling dice game 

# Rules :

#Loop
    # Ask: roll the dice?
    #If player enters 'y' 
    #   generate two random numbers
    #   print them
    # If player enters 'n'
    #   print thanks message
    # Else
    #   print invalid choice#

while True:

    Decision= input ('Roll the the dice? (y/n): ').lower()
    if Decision == 'y':
        die1 = random.randint (1, 6)
        die2 = random.randint (1, 6)
        print (f'({die1}, {die2})')

        if die1 & die2 == 6:
            print ('GOLDEN ROLL !!!')
            break
    
    
    elif Decision == 'n':
        print ('Thanks for playing')
        break

    else:
        print('invalid choice!')