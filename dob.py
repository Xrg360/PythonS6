import tkinter as tk
from tkinter import messagebox

def display_dob():
    dob = entry.get()
    messagebox.showinfo("Date of Birth", f"Your Date of Birth is {dob}")

root = tk.Tk()
root.title("DOB App")

label = tk.Label(root, text="Enter your Date of Birth:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Display DOB", command=display_dob)
button.pack()

root.mainloop()