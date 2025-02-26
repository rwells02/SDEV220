import tkinter as tk
from tkinter import messagebox

#Handles calculator logic and expressions
class CalcLogic:
    def __init__(self):
        self.expression = ''
    
    def add_to_expression(self, value): #adds number/operator to expression
        self.expression += str(value)
        
    def evaluate_expression(self): #evaluates a returns the result + error message if one occurs
        try:
            result = eval(self.expression)
            self.expression = str(result)
            return result
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Expression')
            self.clear_expression()
            return ''
    
    def clear_expression(self): #resets expression back to empty string
        self.expression = ''

#Testing logic
'''
calc = CalcLogic()

calc.add_to_expression("2+3")    #expect 5
print(calc.evaluate_expression())

calc.add_to_expression("*2")
print(calc.evaluate_expression()) #expect 10

calc.clear_expression()
calc.add_to_expression("10/2")    #expect 5
print(calc.evaluate_expression())

calc.clear_expression()
calc.add_to_expression("5-2")    #expect 3
print(calc.evaluate_expression())
'''

