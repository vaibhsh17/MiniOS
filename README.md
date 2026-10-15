<div align="center">

## MiniOS - Educational Operating System Simulator
</div>

- MiniOS is a python-based educational operating system simulator designed to help students understand the fundamental concepts, resposibilities and working principles of an  Operating System (OS) through an  interactive command-line interface.
- It demonstrate that how an operating system manages files, processes, memory, disk space, users, permissions, CPU scheduling and system resources in a simplified enviourment.


> MiniOS is an educationl simulator, not a real or bootable operating system. It runs as a Python application on an existing operating system such as Windows, Linux or MacOS.

<div align="center">

##  📖 Table of Contents
</div>

- What is an Operating System?
- Purpose of an Operating System
- How does an Operating System Work?
- What is MiniOS?
- How MiniOS Works?
- Features
- Operating System Concepts Demonstrated
- Commands
- Project Structure
- Technologies Used
- Installation and Execution
- Data Persistence
- Limitations
- Learning Objectives
- Future Improvements
- Author

**Main Responsibilities of an OS**

- Process Management: Manages running program and their execution.
- Memory Management: Allocates and releases memory for processes.
- File Management: Organizes files and controls file access.
- CPU Scheduling: Determines which process gets CPU time.
- Device Management: Coordinates access to hardware devices.
- Storage Management: Tracks and manages storage space.
- Security and Protection: Controls access to resources.

<div align="center">

## 🎯Purpose of an Operating System
</div>

The main purpose of an operating system is to make  a computer easier and safer to use while managing its hardware and software resources efficiently.

> Without an operating system, applications would need to handle how many low-level hardware operations themselves.

**An OS helps to**:
- Provide an  interface between the user and the computer.
- Executes and manage programs.
- Allocate CPU time and memory.
- Organize files and storage.
- Control and access to resources.
- Coordinate input and output operations.
- Detect and handle certain errors.
- Use available resources efficiently.

<div align="center">

## ⚙️ How does an Operating system Works?
</div>
A simplified view of How a computer system operates:

```
+-----------------------------+
|            User             |
+-----------------------------+
              |
              v
+-----------------------------+
| Applications / User Commands|
+-----------------------------+
              |
              v
+-----------------------------+
|       Operating System      |
|                             |
|  Process Management         |
|  Memory Management          |
|  File Management            |
|  CPU Scheduling             |
|  Storage & Security         |
+-----------------------------+
              |
              v
+-----------------------------+
|           Hardware          |
| CPU | RAM | Disk | Devices  |
+-----------------------------+
```

**Basic Working Process**
- The user intracts with an application or command interface.
- The application requests an operation from the operating system.
- The OS manages access to resources and perform the required work.
- The hardware executes the relevant operations.
- The result is returned to the application or user.

This is a simplified model; actual operating system use mechanism such as system calls, kernal services, intrrupts, device drivers and hardware protection.

## 🚀 What is MiniOS?

MiniOS is a command-line-based educational project implemented in Python.

Its purpose is to simulate selected operating system concepts so user can explore how resource management
and common system operations work.

MiniOS provides commands for managing virtual processes, memory allocations, file-permissions, disk allocations, and system monitoring.

It is intended for learning, experimentation and understanding basic OS concepts-not for replacing a real operating system.

<div align="center">

## 🔄 How MiniOS Works
</div>

MiniOS starts through its Python entry point main.py, which displays a welcome message and accepts command through an interactive command-line shell.

```
================================
        Welcome to MiniOS
================================
Educational OS Simulator
Type 'help' to see commands.

MiniOS>
```
Command Execution Flow
1. Start: Rum main.py using python.
2. Input: Enter a command at MiniOS> Prompt.
3. Processing: MiniOS identifies the command and its arguments.
4. Module Execution: The relevant Python module performs the requested.
5. Output: MiniOS displays the result, status or error messages.
6. Repeat: The shell waits for the next commands.

For Examole: A memory allocation command is handled by the memory-management module, while a disk allocation command is handled by the disk-management module.

<div align="center">

## ✨ Features
</div>

1. File Management:  Create, write, read and delete files using the command-line interface. File permissions determine whether a user can perform a particular operation.
2. Process Management:  Create simulated process entries, display running processes. Each process can include a process ID, name, burst time, and priority.
3. Memory Management:  allocate memory to named processes, track memory usage, display free memory, and release allocations.
4. CPU Scheduling:
   Deminstrate three scheduling a algorithms:
   - First Come, First Served (FCFS)
   - Round Robin
   - Priority Scheduling
  The simulator displays scheduling information and calculated execution time based on the supplied process data.
5. User Management:  Create user account, list users and check login credential through the user-management module.
6. File Permissions:  Demonstrate basic  access control for file reading, writing and deletion.
7. Disk and Storage Management:  Simulate disk-space allocation, freeing allocated space and displaying total, used and free capacity
8. System Monitoring:  Display simulated process information, memory usage, disk usage and overall system statistics thorough a monitoring dashboard.
9. System Commands:  Provide utility commands for displaying the current user, listing files, showing the current directory and date, viewing system information, clearing the terminal and logging out.
10. Data Persistance:  Use JOSN files to retain selected application data between execution,  including user information, and disk allocations.

<div align="center">

## 🧠 Operating System Concepts Demonstrated
</div>

<div align=""center>

| OS Concept | MiniOS Demonstration |
|---|---|
| Process Management | Start, list, and stop simulated processes |
| CPU Scheduling | FCFS, Round Robin, and Priority Scheduling |
| Memory Management | Allocate and release memory |
| File Management | Create, read, write, and delete files |
| Protection | Basic user-based file permissions |
| User Management | User creation and login checks |
| Storage Management | Simulated disk allocation and release |
| Resource Monitoring | Memory, disk, and process statistics |
| Data Persistence | JSON-based application data storage |
| Command Interface | Interactive command-line shell |
</div>

<div align="cenetr">

## ⌨️ Commands
</div>

Type help inside MiniOS to see the commands supported by your current implementation.
File Management

```
create <filename>
write <filename> <content>
read <filename>
delete <filename>
```
Process Management

```
start <name> <burst_time> <priority>
processes
stop <name>
```
Memory Management

```
memory
allocate <process> <size>
free <process>
```
CPU Scheduling

```
fcfs
rr <quantum>
priority
```
User Management

```
createuser <username> <password>
users
login <username> <password>
```
Disk Management

```
disk
diskinfo
allocate_disk <filename> <size>
free_disk <filename>
```
System Monitoring

```
system_status
process_monitor
memory_monitor
disk_monitor
system_statistics
dashboard
```
System Utilities

```
whoami
pwd
ls
date
systeminfo
clear
logout
```
Note:  Command name and argument formats must match the implementation in main.py. Use help to confirm the commands available in your current version.

<div align="center">

## 📂 Project Structure
</div>

```
MiniOS/
├── main.py
├── file_manager.py
├── process_manager.py
├── memory_manager.py
├── cpu_schedulor.py
├── user_manager.py
├── disk_manager.py
├── system_monitor.py
├── .gitignore
└── README.md
```
Module Responsibilities


| File | Responsibility |
|---|---|
| `main.py` | Main entry point, command loop, and command routing |
| `file_manager.py` | File operations and file permissions |
| `process_manager.py` | Simulated process management |
| `memory_manager.py` | Memory allocation and usage tracking |
| `cpu_schedulor.py` | CPU scheduling algorithms |
| `user_manager.py` | User creation, login checks, and roles |
| `disk_manager.py` | Disk-space allocation and tracking |
| `system_monitor.py` | System status, resource monitoring, and statistics |
| `.gitignore` | Excludes selected local and generated files |
| `README.md` | Project documentation |

<div align="center">

## 🛠️ Technologies Used
</div>

- Python:  Core programming language.
- JSON:    Stores selected application data between runs.
- Command-Line Interface (CLI):  Provides an interactive user interface.
- GitHub:  Version control and project hosting.

## Clone the Repo
```
git clone https://github.com/vaibhsh17/MiniOS.git
````
## Explore commands
```
help
```
- Then try the available commands and observe how MiniOS responds.

<div align="center">

## 💾 Persistence
</div>
MiniOS stores selected information in JSON files.

- users.json — user account data.
- file_permissions.json — file permision records.
- disk_storage.json — disk allocation records.

> These files are generated locally as the application runs and are excluded from version control through .gitignore.

<div align="center">

## 🎓 Learning Goals
</div>

