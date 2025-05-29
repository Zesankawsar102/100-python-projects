import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""

        # Entry widget to display the expression/result
        self.entry = tk.Entry(root, font=('Arial', 20), bd=10, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for (text, row, col, colspan) in [(b[0], b[1], b[2], 1) if len(b) == 3 else b for b in buttons]:
            btn = tk.Button(root, text=text, font=('Arial', 18), bd=5, relief=tk.RAISED,
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        # Configure grid to be resizable
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += char
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
