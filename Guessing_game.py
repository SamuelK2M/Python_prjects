import random
#
# The goal is to guess the number randomly generated by the computer
# 
# condition :
# 1 if the input is > generated number print "too high !"
# 2 if the input is < generated number print "too low !
# if the  generated number == generated number print "Congrats !!! You guessed the Number."
# 
# I need to add a loop to always go back to the input ad break until it found#

 

number = random.randint(1, 100)






while True:
    try:
        guess = int(input('Guess the number between 1 and 100: ').lower())
    except valueError:
        print ('Please enter a valid number')
    
        if guess > 100:
            print ('Number above range. Try again')
        elif  guess < 0 :
            print ('Number below range. Try again')


    if guess > number:
        print('Too High !')
          
    elif guess < number:
        print('Too Low !')
    elif guess == number:
    
        print ('Congrats !!! You guessed the number.')
        break

    

