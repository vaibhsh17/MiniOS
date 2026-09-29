import json
import os

USER_FILE = "users.json"

users = []


def load_users():
    global users

    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            users = json.load(file)
    else:
        users = []


def save_users():
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


def create_user(username, password, role="user"):
    for user in users:
        if user["username"] == username:
            print("User already exists.")
            return


    user = {
        "username": username,
        "password": password,
        "role": role
    }


    users.append(user)
    save_users()

    print(f"User '{username}' created successfully.")

def list_users():
    if not users:
        print("No user found.")
        return

    print("\nUsername\tRole")
    print("--------------------")

    for user in users:
        print(f"{user['username']}\t\t{user['role']}")


def login_user(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"Login successful. Welcome, {username}!")
            return True


    print("Invalid username or password.")
    return False


def get_user_role(username):
    for user in users:
        if user["username"] == username:
            return user["role"]

    return None

load_users()