'''
Author: Rashan Wells
Date: 01/27/2025
Version: 1.0
Program: secretNumberGuess.py
'''
secret = 7
guess = 3

if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else:
    print('just right')