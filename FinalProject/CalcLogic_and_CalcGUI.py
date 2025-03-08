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

class CalcGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator GUI")
        self.logic = CalcLogic()
        
        self.display = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
        ('7', 1, 0), ('7', 1, 1), ('7', 1, 2), ('7', 1, 3),
        ('4', 2, 0), ('7', 2, 1), ('7', 2, 2), ('7', 2, 3),
        ('1', 3, 0), ('7', 3, 1), ('7', 3, 2), ('7', 3, 3),
        ('0', 4, 0), ('7', 4, 1), ('7', 4, 2), ('7', 4, 3),
        ('C', 5, 0), ('7', 5, 1),
        ]
        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, font=("Arial", 18), padx=20, pady=20,
                            command=lambda t=text: self.on_btton_use(t))
            btn.grid(row=row, column=col, sticky="nsew")
        
        def on_button_use(self, char):
            if char == "=":
                result = self.logic.evaluate_expression()
                self.update_display(result)
            elif char == "C":
                self.logic.clear_expression()
                self.update_display("")
            else:
                self.logic.add_to_expression(char)
                self.update_display(self.logic.expression)
        
        def update_display(self, value):
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, value)
            
        
        

