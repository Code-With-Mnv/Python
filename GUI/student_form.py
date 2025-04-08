import tkinter as tk
from tkinter import messagebox

def display_info():
    name = entry_name.get()
    age = entry_age.get()
    branch = entry_branch.get()
    games = entry_games.get()
    
    if not name or not age or not branch or not games:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    result = f"Name: {name}\nAge: {age}\nBranch: {branch}\nFavourite Games: {games}"
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, result)

root = tk.Tk()
root.title("Student Form")
root.geometry("450x400")

tk.Label(root, text="Name:").place(x=30, y=30)
entry_name = tk.Entry(root, width=40)
entry_name.place(x=150, y=30)

tk.Label(root, text="Age:").place(x=30, y=70)
entry_age = tk.Entry(root, width=40)
entry_age.place(x=150, y=70)

tk.Label(root, text="Branch:").place(x=30, y=110)
entry_branch = tk.Entry(root, width=40)
entry_branch.place(x=150, y=110)

tk.Label(root, text="Favourite Games:").place(x=30, y=150)
entry_games = tk.Entry(root, width=40)
entry_games.place(x=150, y=150)

tk.Button(root, text="Submit", command=display_info).place(x=180, y=190)

tk.Label(root, text="Student Details:").place(x=30, y=240)
text_box = tk.Text(root, height=8, width=45)
text_box.place(x=30, y=270)

root.mainloop()
