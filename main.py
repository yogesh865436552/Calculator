import tkinter as tk
from tkinter import messagebox
import json
import os  



class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("600x600")
        self.root.configure(bg="#000000")
        self.equation = ""

        # left side for main calculator
        self.calc_frame = tk.Frame(root, bg="#000000")
        self.calc_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # right side for history
        self.history_frame = tk.Frame(root, bg="#1a1a1a", width=200)
        self.history_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        tk.Label(
            self.history_frame,
            text="History",
            font=("Arial", 14, "bold"),
            bg="#1a1a1a",
            fg="#D4AF37"
        ).pack(pady=10)

        self.history_list = tk.Listbox(
            self.history_frame,
            font=("Arial", 12),
            bg="#000000",
            fg="#FFFFFF",
            borderwidth=0,
            highlightthickness=0
        )
        self.history_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # clear history button
        tk.Button(
            self.history_frame,
            text="Clear",
            command=self.clear_history,
            bg="#333333",
            fg="#FFFFFF",
            font=("Arial", 10),
            borderwidth=0
        ).pack(fill=tk.X, padx=5, pady=5)

        self.display = tk.Entry(
            self.calc_frame,
            font=("Arial", 36, "bold"),
            bg="#000000",
            fg="#FFFFFF",
            borderwidth=0,
            justify="right"
        )
        self.display.grid(
            row=0, column=0, columnspan=4,
            sticky="nsew", padx=10, pady=40
        )

        self.create_buttons()

        #keyboard support - much faster than clicking buttons
        self.root.bind("<Key>", self.key_press)
     

    def create_buttons(self):
        # grey for numbers, gold for operators
        num_bg = "#EEEEEE"
        num_fg = "#000000"
        op_fg  = "#D4AF37"

        buttons = [
            ("C", num_bg, op_fg), ("DEL", num_bg, op_fg),
            ("%", num_bg, op_fg), ("/", num_bg, op_fg),
            ("7", num_bg, num_fg), ("8", num_bg, num_fg),
            ("9", num_bg, num_fg), ("*", num_bg, op_fg),
            ("4", num_bg, num_fg), ("5", num_bg, num_fg),
            ("6", num_bg, num_fg), ("-", num_bg, op_fg),
            ("1", num_bg, num_fg), ("2", num_bg, num_fg),
            ("3", num_bg, num_fg), ("+", num_bg, op_fg),
            ("0", num_bg, num_fg), (".", num_bg, num_fg),
            ("=", "#000000", "#FFFFFF")
        ]

        row, col = 1, 0
        for (text, bg, fg) in buttons:
            action = lambda x=text: self.on_click(x)
            columnspan = 2 if text == "=" else 1
            btn = tk.Button(
                self.calc_frame,
                text=text,
                command=action,
                font=("Arial", 20, "bold"),
                bg=bg,
                fg=fg,
                borderwidth=0,
                relief="flat"
            )
            btn.grid(
                row=row, column=col,
                columnspan=columnspan,
                sticky="nsew", padx=1, pady=1
            )
            col += columnspan
            if col >= 4:
                col = 0
                row += 1

        for i in range(1, 6):
            self.calc_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.calc_frame.columnconfigure(i, weight=1)

    def key_press(self, event):
    # handle all keyboard input in one place
        allowed = '0123456789+-*/.%'
        if event.char in allowed:
           self.on_click(event.char)
        elif event.keysym == "Return":
            self.on_click("=")
        elif event.keysym == "BackSpace":
            self.on_click("DEL")
        elif event.keysym == "Escape":
            self.on_click("C")
                

    def on_click(self, char):
        if char == "C":
            self.equation = ""
            self.display.delete(0, tk.END)
        elif char == "DEL":
            self.equation = self.equation[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.equation)
        elif char == "=":
            try:
                result = str(eval(self.equation))
                # save to history before replacing equation
                self.history_list.insert(0, f"{self.equation} = {result}")
                self.equation = result
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception:
                messagebox.showerror("Error", "Invalid input")
                self.equation = ""
                self.display.delete(0, tk.END)
        else:
            self.equation += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.equation)

    def clear_history(self):
        self.history_list.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
