import tkinter as tk
import re

def validate_password():
    password = password_entry.get()
    
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'

    if re.match(pattern, password):
        result_label.config(text="Password is valid!", fg="green")
    else:
        result_label.config(
            text="Invalid Password!\nMust be 8+ characters with uppercase, lowercase, digit & special character.",
            fg="red"
        )


root = tk.Tk()
root.title("Password Validator")
root.geometry("400x250")
root.resizable(False, False)


title = tk.Label(root, text="Enter Password to Validate", font=("Helvetica", 14, "bold"))
title.pack(pady=15)

password_entry = tk.Entry(root, show="*", font=("Helvetica", 12), width=30)
password_entry.pack(pady=10)

validate_btn = tk.Button(root, text="Validate", command=validate_password, font=("Helvetica", 12))
validate_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 11), wraplength=350, justify="center")
result_label.pack(pady=15)

root.mainloop()

