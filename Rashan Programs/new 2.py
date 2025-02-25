import tkinter as tk
from tkinter import messagebox

class CalculatorLogic:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, value):
        self.expression += str(value)

    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            return result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear_expression()
            return ""

    def clear_expression(self):
        self.expression = ""


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.logic = CalculatorLogic()
        
        self.display = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)
        
        self.create_buttons()
    
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0),
        ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, font=("Arial", 18), padx=20, pady=20, 
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew")
        
    def on_button_click(self, char):
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


class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.gui = CalculatorGUI(self.root)
    
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MainApp()
    app.run()
