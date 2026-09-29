processes = []
next_pid = 1

def start_process(name, burst_time, priority):
    global next_pid

    process = {
        "pid": next_pid,
        "name": name,
        "burst_time": burst_time,
        "priority": priority
    }

    processes.append(process)

    print(
        f"process '{name}' started"
        f"with burst time {burst_time} ms."
        f"and priority {priority}."
    )

    next_pid += 1


def list_processes():
    if not processes:
        print("No running processes.")
        return

    print("\nPID\tProcess")
    print("----------------")

    for process in processes:
        print(f"{process['pid']}\t{process['name']}")


def stop_process(name):
    for process in processes:
        if process["name"] == name:
            processes.remove(process)
            print(f"process '{name}' stopped")
            return

    print("Process not found.")