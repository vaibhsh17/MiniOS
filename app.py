from flask import Flask, jsonify, request, send_from_directory
from contextlib import redirect_stdout
from io import StringIO

from process_manager import start_process, list_processes, stop_process, get_processes
from cpu_schedulor import (
    fcfs_schedule,
    round_robin_schedule,
    priority_schedule,
    compare_scheduling
)
from memory_manager import show_memory
from file_manager import create_file, write_file, read_file, delete_file
from disk_manager import show_disk, disk_info, allocate_disk, free_disk_space
import os

app = Flask(
     __name__,
     static_folder="MiniOS-Explorer",
     static_url_path=""
)


@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/health")
def health():
    return jsonify({
        "status": "connected",
        "message": "MiniOS backend is running!"
    })

@app.route("/api/command", methods=["POST"])
def execute_command():
    data = request.get_json(silent=True) or {}
    raw_command = data.get("command", "").strip()

    if not raw_command:
        return jsonify({
            "success": False,
            "output": "Please enter a command."
        }), 400

    command = raw_command.lower()
    parts = raw_command.split()

    output = StringIO()

    if command == "help":
        result = (
            "Available commands:\n"
            "help - Show available commands\n"
            "info - Show MiniOS information\n"
            "processes - Show running prcesses\n"
            "start <name> <burst_time> <priority> - Start a process\n"
            "stop <name> - Stop a process\n"
            "memory - Show memory information\n"
            "create <filename> - Create a file\n"
            "write <filename> <content> - Write content to a file\n"
            "read <filename> - Read a file\n"
            "delete <filename> - Delete a file\n"
            "disk - Show disk status\n"
            "diskinfo - Show disk information\n"
            "allocate_disk <filename> <size> - Allocate disk space\n"
            "free_disk <filename> - Free allocated disk space\n"
            "fcfs - Run First Come First served scheduling\n"
            "rr <quantom> - Run Round Robin Schedling\n"
            "priority - Run Priority Scheduling\n"
            "compare <quantom> - Compare CPU Scheduling Algorithms\n"
        )

    elif command == "info":
        result = (
            "MiniOS version 1.0\n"
            "Educational Operating System Simulator")

    elif command == "processes":
        with redirect_stdout(output):
            list_processes()
        result = output.getvalue() or "No process information available."

    elif parts[0].lower() == "start":
        if len(parts) != 4:
            result = "Usage: start <process_name> <burst_time> <priority>"
        else:
            try:
                name = parts[1]
                burst_time = int(parts[2])
                priority = int(parts[3])

                with redirect_stdout(output):
                    start_process(name, burst_time, priority)

                result = output.getvalue() or f"Process '{name}' started."

            except ValueError:
                result = "Burst time and priority must be numbers."

    elif parts[0].lower() == "stop":
        if len(parts) < 2:
            result = "Usage: stop <process_name>"
        else:
            name = " ".join(parts[1:])

            with redirect_stdout(output):
                stop_process(name)

            result = output.getvalue() or f"stop command sent for `{name}`."

    elif command == "fcfs":
        processes = get_processes()

        with redirect_stdout(output):
            fcfs_schedule(processes)

        result = output.getvalue()

    elif parts[0].lower() == "rr":
        if len(parts) != 2:
            result = "Usage: rr <quantom>"
        else:
            try:
                quantom = int(parts[1])
                processes = get_processes()

                with redirect_stdout(output):
                    round_robin_schedule(processes, quantom)

                result = output.getvalue()

            except ValueError:
                result = "Quantom must be a number."

    elif command == "priority":
        processes = get_processes()

        with redirect_stdout(output):
            priority_schedule(processes)

        result = output.getvalue()

    elif parts[0].lower() == "create":
        if len(parts) != 2:
            result = "Usage: create <filename>"
        else:
            filename = parts[1]

            if not os.path.basename(filename) == filename or filename in (".", "..") or ":" in filename:
                result = "Invalid filename."
            else:
                with redirect_stdout(output):
                    create_file(filename)

                result = output.getvalue() or "File creation completed."

    elif parts[0].lower() == "write":
        write_parts = raw_command.split(maxsplit=2)

        if len(write_parts) != 3:
            result = "Usage: write <filename> <content>"
        else:
            filename = write_parts[1]
            content = write_parts[2]

            if not os.path.basename(filename) == filename or filename in (".", "..") or ":" in filename:
                result = "Invalid filename."
            else:
                with redirect_stdout(output):
                    write_file(filename, content)

                result = output.getvalue() or "Write operation completed."

    elif parts[0].lower() == "read":
        if len(parts) != 2:
            result = "Usage: read <filename>"
        else:
            filename = parts[1]

            if not os.path.basename(filename) == filename or filename in (".", "..") or ":" in filename:
                result = "Invalid filename."
            else:
                with redirect_stdout(output):
                    read_file(filename)

                result = output.getvalue() or "Read operation comleted."

    elif parts[0].lower() == "delete":
        if len(parts) != 2:
            result = "Usage: delete <filename>"
        else:
            filename = parts[1]

            if not os.path.basename(filename) == filename or filename in (".", "..") or ":" in filename:
                result = "Invalid filename."
            else:
                with redirect_stdout(output):
                    delete_file(filename)

                result = output.getvalue() or "Delete operation completed."
                
    elif command == "memory":
        with redirect_stdout(output):
            show_memory()
        result = output.getvalue() or "No memory information available."

    elif command == "disk":
        with redirect_stdout(output):
            show_disk()
        result = output.getvalue() or "No disk information available."

    elif command == "diskinfo":
        with redirect_stdout(output):
            disk_info()
        result = output.getvalue() or "No disk details available."

    elif parts[0].lower() == "allocate_disk":
        if len(parts) != 3:
            result = "Usage: allocate_disk <filename> <size_in_MB>"
        else:
            filename = parts[1]

            if os.path.basename(filename) != filename or filename in (".", "..")or ":" in filename:
                result = "Invalid filename."
            else:
                try:
                    size = int(parts[2])

                    with redirect_stdout(output):
                        allocate_disk(filename, size)

                    result = output.getvalue() or "Disk allocation completed."

                except ValueError:
                    result = "Disk size must be a number."

    elif parts[0].lower() == "free_disk":
        if len(parts) != 2:
            result = "Usage: free_disk <filename>"
        else:
            filename = parts[1]

            if os.path.basename(filename) != filename or filename in (".", "..") or ":" in filename:
                result = "Invalid filename."
            else:
                with redirect_stdout(output):
                    free_disk_space(filename)

                result = output.getvalue() or "Disk space operation completed."

    elif parts[0].lower() == "compare":
        if len(parts) != 2:
            result = "Usage: compare <quantum>"
        else:
            try:
                quantum = int(parts[1])

                with redirect_stdout(output):
                    compare_scheduling(get_processes(), quantum)

                result = output.getvalue()

            except ValueError:
                result = "Quantum must be a number."


    else:
        return jsonify({
            "success": False,
            "output": "Unknown command. Type 'help' to see available commands."
        }), 400

    return jsonify({
        "success": True,
        "output": result
    })

if __name__ == "__main__":
    app.run(debug=True)