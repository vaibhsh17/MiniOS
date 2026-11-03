def fcfs_schedule(processes):
    if not processes:
        print("No processes available for scheduling.")
        return

    print("\n==============================")
    print("     FCFS CPU Scheduling")
    print("==============================")

    print("Process\tBurst\tWaiting\tTurnaround")
    print("----------------------------------------")

    current_time = 0
    total_wt = 0
    total_tat = 0

    for process in processes:
        name = process["name"]
        burst_time = process["burst_time"]

        waiting_time = current_time
        turnaround_time = waiting_time + burst_time

        print(
            f"{name}\t{burst_time}\t"
            f"{waiting_time}\t{turnaround_time}"
        )

        total_wt += waiting_time
        total_tat += turnaround_time

        current_time += burst_time

    count = len(processes)

    print("----------------------------------------")
    print(f"Average Waiting Time: {total_wt / count:.2f} ms")
    print(f"Average Turnaround Time: {total_tat / count:.2f} ms")


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

    remaining_time = {
        process["pid"]: process["burst_time"]
        for process in processes
    }

    completion_time = {}
    total_time = 0

    while any(time > 0 for time in remaining_time.values()):
        for process in processes:
            pid = process["pid"]
            name = process["name"]

            if remaining_time[pid] <= 0:
                continue

            run_time = min(quantum, remaining_time[pid])

            print(f"{name} -> {run_time} ms")

            remaining_time[pid] -= run_time
            total_time += run_time

            if remaining_time[pid] == 0:
                completion_time[pid] = total_time

    print("\nProcess\tBurst\tWaiting\tTurnaround")
    print("----------------------------------------")

    total_wt = 0
    total_tat = 0

    for process in processes:
        pid = process["pid"]
        name = process["name"]
        burst_time = process["burst_time"]

        turnaround_time = completion_time[pid]
        waiting_time = turnaround_time - burst_time

        print(
            f"{name}\t{burst_time}\t"
            f"{waiting_time}\t{turnaround_time}"
        )

        total_wt += waiting_time
        total_tat += turnaround_time

    count = len(processes)

    print("----------------------------------------")
    print(f"Average Waiting Time: {total_wt / count:.2f} ms")
    print(f"Average Turnaround Time: {total_tat / count:.2f} ms")
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

    current_time = 0
    total_wt = 0
    total_tat = 0

    print("Process\tBurst\tPriority\tWaiting\tTurnaround")
    print("------------------------------------------------")

    for process in sorted_processes:
        name = process["name"]
        burst_time = process["burst_time"]
        priority = process["priority"]

        waiting_time = current_time
        turnaround_time = waiting_time + burst_time

        print(
            f"{name}\t{burst_time}\t{priority}\t\t"
            f"{waiting_time}\t{turnaround_time}"
        )

        total_wt += waiting_time
        total_tat += turnaround_time
        current_time += burst_time

    count = len(sorted_processes)

    print("------------------------------------------------")
    print(f"Average Waiting Time: {total_wt / count:2f} ms")
    print(f"Average Turnaround Time: {total_tat / count:2f} ms")
    print(f"Total CPU Time: {current_time} ms")

def compare_scheduling(processes, quantom):
    if not processes:
        print("No processes available for comparison.")
        return

    if quantom <= 0:
        print("Time quantom must be greater than 0.")
        return

    algorithms = [
        ("FCFS", processes),
        ("Round Robin", processes),
        ("Priority", sorted(
            processes,
            key=lambda process: process["priority"]
        ))
    ]

    print("\n==============================")
    print("     CPU SCHEDULING COMPARISON")
    print("==============================")
    print("Algorithm\tAvg Waiting\tAvg Turnaround")
    print("------------------------------------------------")

    for algorithm, process_list in algorithms:
        remaining = {
            p["pid"]: p["burst_time"]
            for p in process_list
        }

        current_time = 0
        completion = {}

        if algorithm == "Round Robin":
            while any(t > 0 for t in remaining.values()):
                for p in process_list:
                    pid = p["pid"]

                    if remaining[pid] <= 0:
                        continue

                    run_time = min(quantom, remaining[pid])
                    remaining[pid] -= run_time
                    current_time += run_time

                    if remaining[pid] == 0:
                        completion[pid] = current_time
        else:
            for p in process_list:
                pid = p["pid"]
                current_time += p["burst_time"]
                completion[pid] = current_time

        total_wt = 0
        total_tat = 0

        for p in process_list:
            pid = p["pid"]
            tat = completion[pid]
            wt = tat - p["burst_time"]

            total_wt += wt
            total_tat += tat

        count = len(process_list)

        avg_wt = total_wt / count
        avg_tat = total_tat / count

        print(
            f"{algorithm}\t\t{avg_wt:.2f} ms"
            f"\t\t{avg_tat:.2f} ms"
        )

    print("==============================")