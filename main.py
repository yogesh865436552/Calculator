import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("600x600")
        self.root.configure(bg="#000000")
        self.equation = ""

        self.calc_frame = tk.Frame(root, bg="#000000")
        self.calc_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.history_frame = tk.Frame(root, bg="#1a1a1a", width=200)
        self.history_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        tk.Label(
            self.history_frame,
            text="HISTORY",
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

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
