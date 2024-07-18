# Author : Manav
# Task : Passowrd Manager

import random

user_pass = []

def generate_pass():

    web_app = input("Enter the name of platform: ")
    user_name = input("Enter your username: ")
    nos = "1234567890"
    sym = "@#&"

    web_pass = ""
    
    for a in range(0,5):
        web_pass = web_pass+ web_app[a]

    user_pass = ""

    for b in range(0, 5):
        user_pass = user_pass + user_name[b]

    no = random.choice(nos)

    s = random.choice(sym)

    password = user_pass + no + s + web_pass
    return password

def generate_username(name):

    extras = "0123456789@#$&"

    up_lim = random.randint(0, len(name))
    user_name = ""

    for i in range (0, up_lim):
        user_name = user_name + name[i]

    for i in range (0, 4):
        user_name = user_name + random.choice(extras)

    return user_name

def add_acc():

    website_app = input("Enter the platform: ")
    print()
    ch0 = input("Have you thought of any username?(y/n):  ")
    print()

    if ch0 in "Yy":
        username = input("Enter your username: ")
    else:
        print("No worries! We have got your back!")

        satisfied = False
        name = input("Enter your name: ")

        while satisfied == False:

            username = generate_username(name)
            print()
            ch1 = input(f"Username: {username} is acceptable? (y/n):  ")

            if ch1 in "Yy":
                print("Username added to list!")
                satisfied = True
            else:
                print("Username not acceptable! Try again.")

    ch = input("Do you have your own password: (y/n) ")
    print()

    if ch in "Nn":
        print("No worries! System will generate a strong password!")
        password = generate_pass()
        print("System generated passowrd is: ", password)
    else:
        password = input("Enter your password: ")

    account = [website_app, username, password]
    user_pass.append(account)
    print()
    print("Account details added successfully!")

def view_acc():

    print()
    web_app = input("Which platform's username and password do you want to see: ")

    for acc in user_pass:

        if acc[0].lower() == web_app.lower():
            print(f"Platform: {acc[0]}")
            print(f"Username: {acc[1]}")
            print(f"Password: {acc[2]}")

        else:
            print("Account not found.")
            ch = input("Want to create one? (y/n): ")

            if ch.lower() == "y":
                add_acc()
            else:
                print("Thank you!")
                break

def edit_acc():
    print()
    web_app = input("Which platform's username and password do you want to edit: ")

    for acc in user_pass:

        if acc[0].lower() == web_app.lower():

            edit = input("What do you want to edit: (username/password): ")

            if edit.lower() == "username":

                ch0 = input("Have you thought of any username?(y/n):  ")
                print()

                if ch0 in "Yy":
                    username = input("Enter your username: ")
                    acc[1] = username

                else:
                    print("No worries! We have got your back!")

                    satisfied = False
                    name = input("Enter your name: ")

                    while satisfied == False:

                        username = generate_username(name)
                        print()
                        ch1 = input(f"Username: {username} is acceptable? (y/n):  ")

                        if ch1 in "Yy":
                            acc[1] = username
                            satisfied = True
                        else:
                            print("Username not acceptable! Try again.")
                print("Username Edited Sucessfully!")

            else:
                ch = input("Do you have your own password: (y/n) ")
                print()

                if ch in "Nn":
                    print("No worries! System will generate a strong password!")
                    password = generate_pass()
                    acc[2] = password
                else:
                    password = input("Enter your password: ")
                    acc[2] = password
                print("Password Edited Succesfully!")

def del_acc():
    print()
    web_app = input("Which platform's data do you want to delete: ")

    for acc in user_pass:

        if acc[0].lower() == web_app.lower():
            user_pass.remove(acc)
            print("Account deleted successfully!")
            break

while True:
    
    print("Welcome to Py_Password_Manager!")
    print()
    print()

    print("What do you want to do: ")
    print("""
            1. Add account
            2. View account
            3. Generate Username
            4. Generate Password
            5. Edit account details
            6. Delete account
          
          """)
    
    choice = int(input("Enter the task number you want to perform: "))
    
    if choice == 1:
        add_acc()
    elif choice == 2:
        view_acc()
    elif choice == 3:
        name = input("Enter your name for username generation: ")
        user = generate_username(name)
        print("The username: ", user)
    elif choice == 4:
        passw = generate_pass()
        print("System generated password: ", passw)
    elif choice == 5:
        edit_acc()
    elif choice == 6:
        del_acc()
    else:
        print("Invalid Choice! Try Again!")
        continue

    ch0 = input("Do you want to perform any other task (y/n): ")
    if ch0 in "yY":
        continue
    else:
        print("Thank you for using PyPassManager!")
        break