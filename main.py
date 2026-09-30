import os
from datetime import datetime
from file_manager import create_file, write_file, read_file, delete_file
from process_manager import start_process, list_processes, stop_process, processes
from memory_manager import show_memory, allocate_memory, free_memory
from cpu_schedulor import fcfs_schedule, round_robin_schedule, priority_schedule
from user_manager import create_user, list_users, login_user, get_user_role

def clear_screen():
    os.system("cls")
    print("""
================================
        Welcome to MiniOS
================================
Educational OS Simulator
Type 'help' to see commands.
""")

def show_info():
    print("""
===============================
           MiniOS
===============================
Educational Operating System
Simulator
Version: 1.0
Language: Python
===============================
""")

def show_help():
    print("""
Available Commands:

help    - Show available commands
info    - Show MiniOS information
clear   - Clear the screen
echo    - Print a message
exit    - Shutdown MiniOS
create  - Create a new file
write   - Write data to a file
read    - Read data from a file
delete  - Delete a file
start   - Start a new process
processes   - Show running process
stop    - Stop a process
memory  - Show memory status
allocate    - Allocate memory to a process
free    - Free memory from a process
schedule    - Run FCFS CPU scheduling
rr  - Run Round Robin CPU scheduling
priority    - Run Priority CPU scheduling
create_user - Create a new user
users   - Show all users
login   - Login as user
role    - Show user role
whoami  - Show current logged-in user
pwd - Show current working directory
ls  - List files and folders
date    - Show current date and time
systeminfo  - Show system information
""")

def start_minios():
    print("""
================================
        Welcome to MiniOS
================================
Educational OS Simulator
Type 'help' to see commands.
""")

    current_user = "admin"

    while True:
        command = input("MiniOS> ")

        if command == "help":
            show_help()

        elif command == "info":
            show_info()

        elif command == "clear":
            clear_screen()

        elif command.startswith("create "):
            filename = command[7:]
            create_file(filename, current_user)

        elif command.startswith("create_user "):
            parts = command.split()

            if len(parts) not in [3, 4]:
                print("Usage: create_user <username> <password> [role]")
            else:
                username = parts[1]
                password = parts[2]
                role = parts[3] if len(parts) == 4 else "user"

                if role not in ["user", "admin"]:
                    print("Role must be 'user' or 'admin'.")
                else:
                    create_user(username, password, role)

        elif command == "users":
                list_users()

        elif command.startswith("write "):
            parts = command.split(" ", 2)

            if len(parts) < 3:
                print("Usage: write <filename> <content>")
            else:
                filename = parts[1]
                content = parts[2]
                write_file(filename, content, current_user)

        elif command.startswith("login "):
            parts = command.split()

            if len(parts) != 3:
                print("Usage: login <username> <password>")
            else:
                username = parts[1]
                password = parts[2]

                if login_user(username, password):
                    current_user = username

        elif command.startswith("role "):
            username = command[5:]

            role = get_user_role(username)

            if role:
                print(f"User '{username}' has role: {role}")
            else:
                print("User not found.")


        elif command == "logout":
            current_user = "guest"
            print("Logged out successfully.")

        elif command == "whoami":
            print(f"current user: {current_user}")

        elif command == "pwd":
            print(os.getcwd())

        elif command == "ls":
            files = os.listdir()

            if not files:
                print("Directory is empty.")
            else:
                print("\nFiles and Folders")
                print("--------------------")

                for item in files:
                    print(item)

        elif command == "date":
            current_date = datetime.now()
            print(current_date.strftime("%d-%m-%Y %H:%M:%S"))

        elif command == "systeminfo":
            print("""
===============================
        System Information
===============================
OS Name: MiniOS
Version: 1.0
Language: Python
""")
            print(f"Current_User: {current_user}")
            print(f"Working Directory: {os.getcwd()}")
            print("===============================")

        elif command.startswith("role "):
            username = command[5:]

            role = get_user_role(username)

            if role:
                print(f"User '{username}' has role: {role}")
            else:
                print("User not found.")


        elif command.startswith("read "):
            filename = command[5:]
            read_file(filename, current_user)

        elif command.startswith("delete "):
            filename = command[7:]
            delete_file(filename, current_user)

        elif command.startswith("start "):
            parts = command.split()

            if len(parts) != 4:
                print("Usage: start <process> <burst_time> <priority>")
            else:
                name = parts[1]

                try:
                    burst_time = int(parts[2])
                    priority = int(parts[3])

                    start_process(name, burst_time, priority)

                except ValueError:
                    print("Burst time and priority must be numbers.")

        elif command == "processes":
            list_processes()

        elif command == "schedule":
            fcfs_schedule(processes)

        elif command.startswith("rr "):
            parts = command.split()

            if len(parts) != 2:
                print("Usage: rr <time_quantum>")
            else:
                try:
                    quantum = int(parts[1])
                    round_robin_schedule(processes, quantum)

                except ValueError:
                    print("Time quantum must be a number.")

        elif command == "priority":
            priority_schedule(processes)

        elif command.startswith("stop "):
            name = command[5:]
            stop_process(name)

        elif command == "memory":
            show_memory()

        elif command.startswith("allocate "):
            parts = command.split()

            if len(parts) != 3:
                print("Usage: allocate <process> <size>")
            else:
                process_name = parts[1]

                try:
                    size = int(parts[2])
                    allocate_memory(process_name, size)

                except ValueError:
                    print("Memory size must be a number.")

        elif command.startswith("free "):
            process_name = command[5:]
            free_memory(process_name)

        
        elif command.startswith("echo "):
            message = command[5:]
            print(message)

        elif command == "exit":
            print("Shutting down MiniOS...")
            break

        else:
            print("Unknown command. Type 'help'.")

start_minios()