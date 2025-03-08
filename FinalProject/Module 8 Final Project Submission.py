import tkinter as tk
from tkinter import messagebox
import math

class CalcLogic:
    def __init__(self):
        self.expression = ''
        self.history = []
        self.expression1 = ''
    
    def add_to_expression(self, value): #adds number/operator to expression
        self.expression += str(value)
        
        
    def evaluate_expression(self): #evaluates a returns the result + error message if one occurs
        try:
            self.expression1 = self.expression
            expression_to_eval = self.expression.rstrip("=")
            result = eval(expression_to_eval, {"__builtins__": None}, {"sin": math.sin, "cos": math.cos, "tan": math.tan, "sqrt": math.sqrt, "pi": math.pi, "radians": math.radians})
            self.expression = str(result)
            self.history.append(f"{self.expression1} = {result}")
            return result
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Expression')
            self.clear_expression()
            return ''
    
    def clear_expression(self): #resets expression back to empty string
        self.expression = ''
        
    def get_history(self):
        return "\n".join(self.history[-5:])  # Show last 5 history items

        

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
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('C', 5, 0), ('S', 7, 0), ('H', 7, 1)
        ]
        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, font=("Arial", 18), padx=20, pady=20,
                            command=lambda t=text: self.on_button_use(t))
            btn.grid(row=row, column=col, sticky="nsew")
        
    def on_button_use(self, char):
        if char == "=":
            result = self.logic.evaluate_expression()
            self.update_display(result)
        elif char == "C":
            self.logic.clear_expression()
            self.update_display("")
        elif char == "S":
            self.open_sci_calc()
        elif char == "H":
            self.show_history()
        else:
            self.logic.add_to_expression(char)
            self.update_display(self.logic.expression)
        
    def update_display(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, value)
        
    def open_sci_calc(self):
        self.root.destroy()  
        root = tk.Tk()  
        SciCalcGUI(root)  
        
    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_text = tk.Text(history_window, height=10, width=30, font=("Arial", 14))
        history_text.pack(padx=10, pady=10)
        history_text.insert(tk.END, self.logic.get_history())
        history_text.config(state=tk.DISABLED)

        
        
        
class SciCalcGUI(CalcGUI):
    def __init__(self, root):
        super().__init__(root)
        self.root.title("Scientific Calculator")
        self.add_sci_buttons()

    def add_sci_buttons(self):
        sci_buttons = [
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('sqrt', 6, 3), ('Back', 7, 3), ('pi', 5, 1), ('(', 5, 2), (')', 5, 3)
        ]
        for (text, row, col) in sci_buttons:
            btn = tk.Button(self.root, text=text, font=("Arial", 18), padx=20, pady=20,
                            command=lambda t=text: self.on_button_use(t))
            btn.grid(row=row, column=col, sticky="nsew")

    def on_button_use(self, char):
        if char == "Back":  
            self.open_standard_calc()
        elif char == "sin":  
            self.logic.add_to_expression(f"{char}(")
            self.update_display(self.logic.expression)
        elif char == "cos":  
            self.logic.add_to_expression(f"{char}(")
            self.update_display(self.logic.expression)
        elif char == "tan":  
            self.logic.add_to_expression(f"{char}(")
            self.update_display(self.logic.expression)
        elif char == "sqrt":  
            self.logic.add_to_expression(f"{char}(")
            self.update_display(self.logic.expression)
        else:
            super().on_button_use(char)

    def open_standard_calc(self):
        self.root.destroy()  
        root = tk.Tk()  
        CalcGUI(root)  


if __name__ == "__main__":
    root = tk.Tk()
    app = CalcGUI(root)
    root.mainloop()
            


            

    
            
        
        

