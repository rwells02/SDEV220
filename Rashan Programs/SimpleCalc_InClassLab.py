'''
SDEV 220-01J In-Class Lab
Author: Rashan Wells
Program: Simple Calculation
Version: 1.0
Date: 1/15/2025
Requirements: 1. Must have at least 4 modules
              2. Must have a menu to choose the math function 
              3. Must be able to add, subtract, multiply and divide            
              4. Division must account for and protect from dividing by zero.
'''
#modules
def getNumInput():
    num1 = 0.0
    num2 = 0.0
    num1 = float(input('Please enter the first number: '))
    num2 = float(input('Please enter the second number: '))
    return num1, num2
    
def getMathFunction():
    operationSymbol = ''
    operationSymbol = input('Please select a mathmatical operation "+": for addition, "-": for subtraction,"/" for division, "*" for multiplication: ')
    return operationSymbol 
    
def myAddition(number1, number2):
    answer = 0.0
    answer = number1 + number2
    return answer

def mySubtraction(number1, number2):
    answer = 0.0
    answer = number1 - number2
    return answer
    
def myMultiplication(number1, number2):
    answer = 0.0
    answer = number1 * number2
    return answer
 
def myDivision(number1, number2):
    answer = 0.0
    if number2 == 0.0:
        answer = 'Undefined, you may not divide by zero.'
    else:
       answer = number1 / number2
    return answer
    
def main():
    #initialization
    CONTROL = "Y"
    userChoice = 'Y'
    num1 = 0.0
    num2 = 0.0
    mathFunction = ''
    finalValue = 0.0
    
    while userChoice == CONTROL:
        
        num1, num2 = getNumInput()
        
        mathFunction = getMathFunction()
        
        if mathFunction == '+':
            finalValue = myAddition(num1, num2)
        elif mathFunction == '-':
            finalValue = mySubtraction(num1, num2)
        elif mathFunction == '*':
            finalValue = myMultiplication(num1, num2)
        elif mathFunction == '/':
            finalValue = myDivision(num1, num2)
        else:
            print('No valid math function was chosen.')

        if finalValue == 'Undefined, you may not divide by zero.':
            print(finalValue)
        else:
            print(f'{num1:.2f} {mathFunction} {num2:.2f} = {finalValue:.2f}')
        
        userChoice = input('Would you like to do another simple calculation? "Y" for yes or "N" for no: ')
        userChoice = userChoice.upper()
               


main()


   
