import memory_manager
import disk_manager


def system_status(processes):
    used_memory = memory_manager.used_memory
    total_memory = memory_manager.TOTAL_MEMORY

    used_disk = disk_manager.used_disk
    total_disk = disk_manager.TOTAL_DISK

    free_memory = total_memory - used_memory
    free_disk = total_disk - used_disk

    print("\n==============================")
    print("     MiniOS System Status")
    print("==============================")

    print(f"Running Processes: {len(processes)}")

    print("\nMemory:")
    print(f"Total Memory: {total_memory} MB")
    print(f"Used Memory: {used_memory} MB")
    print(f"Free Memory: {free_memory} MB")

    print("\nDisk:")
    print(f"Total Disk: {total_disk} MB")
    print(f"Used Disk: {used_disk} MB")
    print(f"Free Disk: {free_disk} MB")

    print("==============================")


def process_monitor(processes):
    print("\n==============================")
    print("     Process Monitor")
    print("==============================")

    if not processes:
        print("No running processes.")
        print("==============================")
        return

    print("PID\tProcess\t\tBurst Time\tPriority")
    print("-----------------------------------------------")

    for process in processes:
        print(
            f"{process['pid']}\t"
            f"{process['name']}\t\t"
            f"{process['burst_time']} ms\t\t"
            f"{process['priority']}"
        )

    print("==============================")


def memory_monitor():
    total_memory = memory_manager.TOTAL_MEMORY
    used_memory = memory_manager.used_memory
    free_memory = total_memory - used_memory

    if total_memory > 0:
        usage_percent = (used_memory / total_memory) * 100
    else:
        usage_percent = 0

    print("\n==============================")
    print("     Memory Monitor")
    print("==============================")

    print(f"Total Memory: {total_memory} MB")
    print(f"Used Memory: {used_memory} MB")
    print(f"Free Memory: {free_memory} MB")
    print(f"Memory Usage: {usage_percent:.2f}%")

    print("==============================")


def disk_monitor():
    total_disk = disk_manager.TOTAL_DISK
    used_disk = disk_manager.used_disk
    free_disk = total_disk - used_disk

    if total_disk > 0:
        usage_percent = (used_disk / total_disk) * 100
    else:
        usage_percent = 0

    print("\n==============================")
    print("     Disk Monitor")
    print("==============================")

    print(f"Total Disk: {total_disk} MB")
    print(f"Used Disk: {used_disk} MB")
    print(f"Free Disk: {free_disk} MB")
    print(f"Disk Usage: {usage_percent:.2f}%")

    print("==============================")


def system_statistics(processes):
    total_memory = memory_manager.TOTAL_MEMORY
    used_memory = memory_manager.used_memory

    total_disk = disk_manager.TOTAL_DISK
    used_disk = disk_manager.used_disk

    if total_memory > 0:
        memory_usage = (used_memory / total_memory) * 100
    else:
        memory_usage = 0

    if total_disk > 0:
        disk_usage = (used_disk / total_disk) * 100
    else:
        disk_usage = 0

    print("\n==============================")
    print("     System Statistics")
    print("==============================")

    print(f"Running Processes:  {len(processes)}")
    print(f"Memory Usage:       {memory_usage:.2f}%")
    print(f"Disk Usage:         {disk_usage:.2f}%")

    print("==============================")


def monitoring_dashboard(processes):
    total_memory = memory_manager.TOTAL_MEMORY
    used_memory = memory_manager.used_memory
    free_memory = total_memory - used_memory

    total_disk = disk_manager.TOTAL_DISK
    used_disk = disk_manager.used_disk
    free_disk = total_disk - used_disk

    if total_memory > 0:
        memory_usage = (used_memory / total_memory) * 100
    else:
        memory_usage = 0

    if total_disk > 0:
        disk_usage = (used_disk / total_disk) * 100
    else:
        memory_usage > 0

    if total_disk > 0:
        disk_usage = (used_disk / total_disk) * 100
    else:
        disk_usage = 0

    print("\n========================================")
    print("     MiniOS Monitoring Dashboard")
    print("========================================")

    print("\nProcesses:")
    print(f"Running Processes: {len(processes)}")

    print("\nMemory:")
    print(f"Total:  {total_memory} MB")
    print(f"Used:   {used_memory} MB")
    print(f"Free:   {free_memory} MB")
    print(f"Usage:  {memory_usage:.2f}%")

    print("\nDisk:")
    print(f"Total:  {total_disk} MB")
    print(f"Used:   {used_disk} MB")
    print(f"Free:   {free_disk} MB")
    print(f"Usage:  {disk_usage:.2f}%")

    print("\n========================================")