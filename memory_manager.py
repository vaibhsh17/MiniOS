TOTAL_MEMORY = 1024
used_memory = 0
allocated_memory = {}

def show_memory():
    free_memory = TOTAL_MEMORY - used_memory

    print("\n==============================")
    print("       Memory Status")
    print("==============================")
    print(f"Total /memory: {TOTAL_MEMORY} MB")
    print(f"Used_Memory: {used_memory} MB")
    print(f"Free_Memory: {free_memory} MB")

def allocate_memory(process_name, size):
    global used_memory

    if size <= 0:
        print("Memory size must be greater than 0.")
        return

    if process_name in allocated_memory:
        print("Memory already allocated i this process.")
        return

    free_memory = TOTAL_MEMORY - used_memory

    if size > free_memory:
            print("Not enough memory available.")
            return

    allocated_memory[process_name] = size
    used_memory += size

    print(f"{size} MB memory allocated to '{process_name}'.")

def free_memory(process_name):
    global used_memory

    if process_name not in allocated_memory:
        print("No memory allocated to this process.")
        return

    size = allocated_memory[process_name]

    used_memory -= size
    del allocated_memory[process_name]

    print(f"{size} MB memory freed from '{process_name}'.")