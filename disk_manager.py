import json
import os

TOTAL_DISK = 10240
used_disk = 0

DISK_FILE = "disk_storage.json"

disk_allocations = {}

def load_disk():
    global disk_allocations
    global used_disk

    if os.path.exists(DISK_FILE):
        with open(DISK_FILE, "r") as file:
            disk_allocations = json.load(file)

        used_disk = sum(disk_allocations.values())
    else:
        disk_allocations = {}
        used_disk = 0

def save_disk():
    with open(DISK_FILE, "w") as file:
        json.dump(disk_allocations, file, indent=4)


def load_disk():
    global disk_allocations
    global used_disk

    if os.path.exists(DISK_FILE):
        with open(DISK_FILE, "r") as file:
            disk_allocations = json.load(file)

        used_disk = sum(disk_allocations.values())
    else:
        disk_allocations = {}
        used_disk = 0


def save_disk():
    with open(DISK_FILE, "w") as file:
        json.dump(disk_allocations, file, indent=4)


def show_disk():
    free_disk = TOTAL_DISK - used_disk

    print("\n==============================")
    print("       Disk Status")
    print("==============================")
    print(f"Total Disk: {TOTAL_DISK} MB")
    print(f"Used Disk: {used_disk} MB")
    print(f"Free Disk: {free_disk} MB")
    print("==============================")


def disk_info():
    print("\n==============================")
    print("       Disk Information")
    print("==============================")
    print("Disk Name: MiniOS Disk")
    print("Disk Type: Virtual Disk")
    print("File System: MiniFS")
    print(f"Total Capacity: {TOTAL_DISK} MB")
    print(f"Used Space: {used_disk} MB")
    print(f"Free Space: {TOTAL_DISK - used_disk} MB")
    print("==============================")


def allocate_disk(filename, size):
    global used_disk

    if size <= 0:
        print("Disk size must be greater than 0.")
        return

    if filename in disk_allocations:
        print("Disk space already allocated to this file.")
        return

    free_disk = TOTAL_DISK - used_disk

    if size > free_disk:
        print("Not enough disk space available.")
        return

    disk_allocations[filename] = size
    used_disk += size

    save_disk()

    print(f"{size} MB disk space allocated to '{filename}'.")


def free_disk_space(filename):
    global used_disk

    if filename not in disk_allocations:
        print("No disk allocated to this file.")
        return

    size = disk_allocations[filename]

    used_disk -= size
    del disk_allocations[filename]

    save_disk()

    print(f"{size} MB disk space freed from '{filename}'.")


load_disk()