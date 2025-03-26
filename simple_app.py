import tkinter as tk
from tkinter import messagebox

def on_submit():
    user_input = entry.get().strip()
    if user_input:
        messagebox.showinfo("Message", f"You entered: {user_input}")
        entry.delete(0, tk.END)  # Clear the input field after submission
        update_character_count()
    else:
        messagebox.showwarning("Warning", "Please enter something!")

def on_clear():
    entry.delete(0, tk.END)
    update_character_count()

def on_exit():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

def update_character_count(event=None):
    count = len(entry.get())
    counter_label.config(text=f"Character count: {count}")

root = tk.Tk()
root.title("Enhanced Python App")
root.geometry("300x220")
root.resizable(False, False)

label = tk.Label(root, text="Enter something:", font=("Arial", 12))
label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)
entry.bind("<KeyRelease>", update_character_count)

counter_label = tk.Label(root, text="Character count: 0", font=("Arial", 10))
counter_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

submit_button = tk.Button(button_frame, text="Submit", command=on_submit, font=("Arial", 12), bg="lightblue")
submit_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=on_clear, font=("Arial", 12), bg="lightgray")
clear_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=on_exit, font=("Arial", 12), fg="red", bg="lightcoral")
exit_button.grid(row=0, column=2, padx=5)

root.mainloop()
