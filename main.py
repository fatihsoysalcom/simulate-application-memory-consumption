import sys

def create_large_list_of_strings(num_elements, avg_string_length):
    """
    Creates a list of strings to simulate memory consumption.
    Each string will have approximately `avg_string_length` characters.
    """
    print(f"Creating a list with {num_elements} strings, each ~{avg_string_length} chars long...")
    data = []
    # Create strings of the specified length. `sys.getsizeof` will estimate their memory.
    for i in range(num_elements):
        data.append('x' * avg_string_length)
    return data

def estimate_list_of_strings_size(data_list):
    """
    Estimates the total memory in bytes consumed by a list of strings.
    This includes the list object itself and all string objects it contains.
    """
    if not data_list:
        return sys.getsizeof([]) # Size of an empty list

    total_size = sys.getsizeof(data_list) # Size of the list object itself
    for item in data_list:
        total_size += sys.getsizeof(item) # Add size of each string object
    return total_size

# --- Main simulation ---
print("--- Python Memory Consumption Simulation ---")
print("This script demonstrates how applications can consume significant RAM.")
print("It estimates memory usage by Python objects, not total system RAM,")
print("but illustrates the concept of accumulating memory footprint.")
print("-" * 60)

# Scenario 1: Main application (e.g., a web browser with many tabs)
# This simulates a primary application holding a large amount of data.
main_app_elements = 10_000_000 # 10 million strings
main_app_string_length = 100 # characters per string
main_app_data = create_large_list_of_strings(main_app_elements, main_app_string_length)
main_app_size_bytes = estimate_list_of_strings_size(main_app_data)
print(f"Main application data estimated size: {main_app_size_bytes / (1024**2):.2f} MB")
print("-" * 60)

# Scenario 2: Background process 1 (e.g., a chat application, cloud sync client)
# This simulates a background process that is always running and consuming memory.
bg_process1_elements = 2_000_000 # 2 million strings
bg_process1_string_length = 50 # characters per string
bg_process1_data = create_large_list_of_strings(bg_process1_elements, bg_process1_string_length)
bg_process1_size_bytes = estimate_list_of_strings_size(bg_process1_data)
print(f"Background process 1 data estimated size: {bg_process1_size_bytes / (1024**2):.2f} MB")
print("-" * 60)

# Scenario 3: Background process 2 (e.g., an IDE, a music player with large library)
# Another background process contributing to overall memory pressure.
bg_process2_elements = 3_000_000 # 3 million strings
bg_process2_string_length = 70 # characters per string
bg_process2_data = create_large_list_of_strings(bg_process2_elements, bg_process2_string_length)
bg_process2_size_bytes = estimate_list_of_strings_size(bg_process2_data)
print(f"Background process 2 data estimated size: {bg_process2_size_bytes / (1024**2):.2f} MB")
print("-" * 60)

total_estimated_app_memory = (main_app_size_bytes + bg_process1_size_bytes + bg_process2_size_bytes)
print(f"Total estimated memory consumed by these 'applications': {total_estimated_app_memory / (1024**3):.2f} GB")
print("\n--- Article Context ---")
print("This example demonstrates how the cumulative memory footprint of active applications")
print("can quickly add up. In a real system, this 'application memory' is in addition to:")
print("1.  Operating System (Windows, macOS, Linux) core processes.")
print("2.  Integrated Graphics (iGPU) memory reservation (often 1-2 GB).")
print("3.  Other system services, drivers, and cached data.")
print("\nThese combined factors explain why a system with 16 GB RAM might feel insufficient,")
print("as the 'effectively available' RAM for your primary tasks is much lower than 16 GB.")
print("For instance, if OS, iGPU, and background services consume 6-8 GB,")
print("and your applications (like this simulation) consume another 2-3 GB,")
print("you're already at 8-11 GB, leaving little headroom for peak loads.")

# Keep references to data lists to prevent them from being garbage collected immediately,
# simulating long-running applications.
_ = [main_app_data, bg_process1_data, bg_process2_data]
