import os
import json

PERMISSION_FILE = "file_permissions.json"

file_permissions = {}


def load_permissions():
    global file_permissions

    if os.path.exists(PERMISSION_FILE):
        with open(PERMISSION_FILE, "r") as file:
            file_permissions = json.load(file)
    else:
        file_permissions = {}

def save_permissions():
    with open(PERMISSION_FILE, "w") as file:
        json.dump(file_permissions, file, indent=4)

def create_file(filename, owner="admin"):
    if os.path.exists(filename):
        print("File already exists.")
        return

    open(filename, "w").close()

    file_permissions[filename] = {
        "owner": owner,
        "read": True,
        "write": True,
        "delete": True
    }

    save_permissions()

    print("File created successfully.")
    print(f"owner: {owner}")


def check_permissions(filename, username, action):

    if username == "admin":
        return True

    if filename not in file_permissions:
        return False

    permission = file_permissions[filename]
    owner = permission["owner"]

    if username == owner:
        return permission[action]

    return False

def write_file(filename, content, username="admin"):
    if not os.path.exists(filename):
        print("File does not exist.")
        return

    if not check_permissions(filename, username, "write"):
        print("Permission denied.")
        return

    with open(filename, "w") as file:
        file.write(content)

    print("Data saved successfully.")


def read_file(filename, username="admin"):
    if not os.path.exists(filename):
        print("File does not exist.")
        return

    if not check_permissions(filename, username, "read"):
        print("Permission denied.")
        return

    with open(filename, "r") as file:
        content = file.read()

    print(content)


def delete_file(filename, username="admin"):
    if not os.path.exists(filename):
        print("File does not exist.")
        return

    if not check_permissions(filename, username, "delete"):
        print("Permission denied.")
        return

    os.remove(filename)

    if filename in file_permissions:
        del file_permissions[filename]

    save_permissions()

    print("File deleted successfully.")


load_permissions()