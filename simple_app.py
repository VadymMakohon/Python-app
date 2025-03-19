import tkinter as tk
from tkinter import messagebox

def on_submit():
    user_input = entry.get().strip()
    if user_input:
        messagebox.showinfo("Message", f"You entered: {user_input}")
        entry.delete(0, tk.END)  # Clear the input field after submission
    else:
        messagebox.showwarning("Warning", "Please enter something!")

def on_exit():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Enhanced Python App")
root.geometry("300x200")
root.resizable(False, False)

# Create input field
label = tk.Label(root, text="Enter something:", font=("Arial", 12))
label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Create button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create submit button
submit_button = tk.Button(button_frame, text="Submit", command=on_submit, font=("Arial", 12))
submit_button.grid(row=0, column=0, padx=5)

# Create exit button
exit_button = tk.Button(button_frame, text="Exit", command=on_exit, font=("Arial", 12), fg="red")
exit_button.grid(row=0, column=1, padx=5)

# Run application
root.mainloop()
