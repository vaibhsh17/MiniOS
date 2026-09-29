def fcfs_schedule(processes):
    if not processes:
        print("No processes available for scheduling.")
        return

    print("\n==============================")
    print("       FCFS CPU Scheduling")
    print("==============================")

    print("Process\tBurst Time")
    print("------------------------------")

    total_time = 0

    for process in processes:
        pid = process["pid"]
        name = process["name"]
        burst_time = process["burst_time"]

        print(f"{name}\t{burst_time} ms")

        total_time += burst_time

    print("------------------------------")
    print(f"Total CPU Time: {total_time} ms")

def round_robin_schedule(processes, quantum):
    if not processes:
        print("No processes available for scheduling.")
        return

    if quantum <= 0:
        print("Time quantum must be greater than 0.")
        return

    print("\n==============================")
    print("     Round Robin Scheduling")
    print("==============================")

    remaining_time = {}

    for process in processes:
        remaining_time[process["pid"]] = process["burst_time"]

    total_time = 0

    while any(time > 0 for time in remaining_time.values()):

        for process in processes:
            pid = process["pid"]
            name = ["name"]

            if remaining_time[pid] <= 0:
                continue

            run_time = min(quantum, remaining_time[pid])

            print(f"{name} -> {run_time} ms")

            remaining_time[pid] -= run_time
            total_time += run_time

    print("------------------------------")
    print(f"Total CPU Time: {total_time} ms")

def priority_schedule(processes):
    if not processes:
        print("No processes available for scheduling.")
        return

    print("\n==============================")
    print("     Priority Scheduling")
    print("==============================")

    sorted_processes = sorted(
        processes,
        key=lambda process: process["priority"]
    )

    total_time = 0

    print("Process\tBurst Time\tPriority")
    print("----------------------------------------")

    for process in sorted_processes:
        name = process["name"]
        burst_time = process["burst_time"]
        priority = process["priority"]

        print(f"{name}]\t{burst_time} ms\t\t{priority}")

        total_time +=burst_time

    print("----------------------------------------")
    print(f"Total CPU Time: {total_time} ms")