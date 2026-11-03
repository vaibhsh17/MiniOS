processes = []
next_pid = 1

def start_process(name, burst_time, priority):
    global next_pid

    process = {
        "pid": next_pid,
        "name": name,
        "burst_time": burst_time,
        "priority": priority,
        "status": "Running"
    }

    processes.append(process)

    print(
        f"Process '{name}' started "
        f"with burst time {burst_time} ms"
        f"and priority {priority}."
    )

    next_pid += 1

def list_processes():
    if not processes:
        print("No processes available.")
        return

    for process in processes:
        print(
            f"{process['pid']}\t"
            f"{process['name']}\t\t"
            f"{process['status']}"
        )

def get_processes():
    return processes.copy()

def stop_process(name):
    for process in processes:
        if process["name"] == name:

            if process["status"] == "Stopped":
                print(f"Process '{name}' is already stopped.")
                return

            process["status"] = "Stopped"
            print(f"Process '{name}' stopped.")
            return

    print("Process not found.")