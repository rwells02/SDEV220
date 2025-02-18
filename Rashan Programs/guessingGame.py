'''
writing a guessing game find a number from 1 to 500
'''
from random import randint 

def getNumberForGame(low, high):
    num = ''
    num = randint(low, high) 
    return num

def compareGuessAndNumber(userGuess, numToGuess):
    answer = ''
    if userGuess > numToGuess:
        answer = 'Too high, try again.'
    else:
        answer = 'You are too low.'
    return answer
        
        
def main():
    #initialization
    NUMBER_TO_GUESS = ''
    LOWER_LIMIT = 1
    UPPER_LIMIT = 500
    usersGuess = ''
    attempt = ''
    playAgain = 'Y'
    
    while playAgain == 'Y':          
        NUMBER_TO_GUESS = getNumberForGame(LOWER_LIMIT, UPPER_LIMIT)
        #print(NUMBER_TO_GUESS)
    
        usersGuess = float(input(f'Please enter an integer between {LOWER_LIMIT} and {UPPER_LIMIT}: '))
        usersGuess = int(usersGuess)
        while usersGuess < LOWER_LIMIT or usersGuess > UPPER_LIMIT:
                if usersGuess < LOWER_LIMIT:
                    print(f"Please enter a number greater than {LOWER_LIMIT}.")
                elif usersGuess > UPPER_LIMIT:
                    print(f"Please enter a number less than {UPPER_LIMIT}.")
                     
                usersGuess = float(input(f'Please enter an integer between {LOWER_LIMIT} and {UPPER_LIMIT}: '))
                usersGuess = int(usersGuess)
        
        
        while usersGuess != NUMBER_TO_GUESS: 
        
            attempt = compareGuessAndNumber(usersGuess, NUMBER_TO_GUESS)
            print(attempt)
            
            usersGuess =  float(input(f'Please enter an integer between {LOWER_LIMIT} and {UPPER_LIMIT}: '))
            usersGuess = int(usersGuess)
            while usersGuess < LOWER_LIMIT or usersGuess > UPPER_LIMIT:
                if usersGuess < LOWER_LIMIT:
                    print(f"Please enter a number greater than {LOWER_LIMIT}.")
                elif usersGuess > UPPER_LIMIT:
                    print(f"Please enter a number less than {UPPER_LIMIT}.")
        
        print(f'\nCongratulations you guessed the correct number: {usersGuess}!')
        
        playAgain = input('Would you like to play again? "Y" for yes or "N" for no: ')
        playAgain = playAgain.upper()
        while (playAgain != 'Y') and (playAgain != 'N'):
            print('Please enter "Y" or "N"')
            playAgain = input('Would you like to play again? "Y" for yes or "N" for no: ')
            playAgain = playAgain.upper()

    print('Thank you for playing our guessing game!')
            
main()
