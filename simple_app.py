import tkinter as tk
from tkinter import messagebox

def on_submit():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Message", f"You entered: {user_input}")
    else:
        messagebox.showwarning("Warning", "Please enter something!")

# Create main window
root = tk.Tk()
root.title("Simple Python App")
root.geometry("300x200")

# Create input field
label = tk.Label(root, text="Enter something:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Run application
root.mainloop()
