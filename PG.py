import tkinter as tk
import string
import random

def generate_password():
    password = []
    for i in range(5):
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(string.punctuation))
        password.append(random.choice(string.digits))

    final_password = "".join(password)
    label.config(text=final_password)

root = tk.Tk()
root.geometry("400x300")
root.title("Password Generator")

button = tk.Button(root, text="Generate Password", command=generate_password)
button.grid(row=1, column=1, padx=20, pady=20)

label = tk.Label(root, font=("Times", 15, "bold"))
label.grid(row=4, column=1)

root.mainloop()