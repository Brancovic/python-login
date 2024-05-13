import json
import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "quit" or password == "quit":
        return

    with open('usernames.json', 'r') as usernames_file:
        username_data = json.load(usernames_file)

    with open('passwords.json', 'r') as passwords_file:
        password_data = json.load(passwords_file)

    if username in username_data['id']:
        index = username_data['id'].index(username)
        if password == password_data['password'][index]:
            messagebox.showinfo("Login Successful", "Welcome, {}!".format(username))
            root.destroy()
        else:
            messagebox.showerror("Login Failed", "Incorrect password.")
    else:
        messagebox.showerror("Login Failed", "Username not found.")

def register():
    username = username_entry.get()
    password = password_entry.get()

    if username == "quit" or password == "quit":
        return

    if "" == username or " " in username:
        messagebox.showerror("Registration Failed", "Invalid arguments (cannot use spaces)")
    else:
        with open('usernames.json', 'r+') as usernames_file:
            usernames_data = json.load(usernames_file)
            usernames_data['id'].append(username)
            usernames_file.seek(0)
            json.dump(usernames_data, usernames_file)

        with open('passwords.json', 'r+') as passwords_file:
            passwords_data = json.load(passwords_file)
            passwords_data['password'].append(password)
            passwords_file.seek(0)
            json.dump(passwords_data, passwords_file)
            messagebox.showinfo("Registration Successful", "User {} registered successfully.".format(username))

def quit_program():
    root.destroy()

root = tk.Tk()
root.title("Login/Register")

username_label = tk.Label(root, text="Enter username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Enter password:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

register_button = tk.Button(root, text="Register", command=register)
register_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

quit_button = tk.Button(root, text="Quit", command=quit_program)
quit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

root.mainloop()
