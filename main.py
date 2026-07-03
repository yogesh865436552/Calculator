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

root.mainloop()
