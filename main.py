import json

# Login part
logged = True

while logged:

    action = input("Enter action you want to make or quit (Login, register, quit): ")
    action = action.lower()

    if action == "login":
        username = input("Enter username: ")
        password = input("Enter {} password: ".format(username))

        if username == "quit" or password == quit:
            print("returning to menu")

        with open('usernames.json', 'r') as usernames_file:
            username_data = json.load(usernames_file)

        with open('passwords.json', 'r') as passwords_file:
            password_data = json.load(passwords_file)

        if username in username_data['id']:
            index = username_data['id'].index(username)
            if password == password_data['password'][index]:
                print("Welcome, {}!".format(username))
                logged = False
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")

    elif action == "register":
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        if username == "quit" or password == "quit":
            print("returning to menu")

        if "" == username or " " in username:
            print("Invalid arguments (cannot use spaces)")
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
                print("User {} registered successfully.".format(username))
    elif action == "quit":
        print("Quitting program")
        break
    else:
        print("False input, try again")
