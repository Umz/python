#   Simple Game to Guess the number between 1 and 10

import random

gen = random.randint(1, 11)
guess = -1;

while not guess == gen:
    print('Guess the number between 1 and 10')
    guessIn = input()
    try:
        guess = int(guessIn)
        if guess > gen:
            print ('Too high')
        elif guess < gen:
            print ('Too low')
    except:
        print('Not a valid integer')
        
print ('Well played')
