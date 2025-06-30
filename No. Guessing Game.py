#Generate a random no.
#Asking the user to make a guess
#if not a valid no
# print error
#if no < guess
# print the no is low
#if no > guess
# print the no is high
#else
# print congrats u have found the no
 
import random

number_to_guess=random.randint(1,100)
while True:
    try:
        guess = int(input('Guess the number between 1 & 100 : '))
    

        if guess < number_to_guess:
            print('Too low')
        elif guess > number_to_guess:
            print('Too high')
        else:
            print('Congrats you guessed it right')
            break
    
    except ValueError:
        print('Enter a valid number') 