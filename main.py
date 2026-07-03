import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("600x600")
root.configure(bg="000000")
root.mainloop()

#main calculator on left side
calc_frame = tk.Frame(root, bg="000000")
calc_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#History sidebar on right
history_frame = tk.Frame(root, bg="#1a1a1a", width=200)
history_frame.pack(side=tk.Right, fill=tk.BOTH)

tk.Label(
    history_frame,
    text="HISTORY",
    FONT=("Arial", 14, "bold"),
    bg="#1a1a1a",
    fg="#D4AF37"
).pack(pady=10)
# display screen for calculator input
display = tk.Entry(
    calc_frame,   
    font=("Arial", 24,"bold"), 
    bg="#1a1a1a", 
    fg="#D4AF37",
    bd=0, 
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

root.mainloop()
