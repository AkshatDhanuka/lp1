def fcfs(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    current_time = 0
    waiting_time = 0

    for process in processes:
        waiting_time += max(0, current_time - process[1])  # Calculate waiting time
        current_time += process[2]  # Update current time

    average_waiting_time = waiting_time / len(processes)
    print(f"FCFS Average Waiting Time: {average_waiting_time:.2f}")

def sjf_preemptive(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time and burst time
    current_time = 0
    waiting_time = 0
    remaining_processes = processes.copy()

    while remaining_processes:
        process = min(remaining_processes, key=lambda x: x[3])  # Choose process with the shortest remaining time
        waiting_time += max(0, current_time - process[1])  # Calculate waiting time
        current_time += 1
        process[2] -= 1  # Decrement remaining time

        if process[2] == 0:
            remaining_processes.remove(process)

    average_waiting_time = waiting_time / len(processes)
    print(f"SJF Preemptive Average Waiting Time: {average_waiting_time:.2f}")

def priority_non_preemptive(processes):
    processes.sort(key=lambda x: (x[1], x[4]))  # Sort by arrival time and priority
    current_time = 0
    waiting_time = 0

    for process in processes:
        waiting_time += max(0, current_time - process[1])  # Calculate waiting time
        current_time += process[2]  # Update current time

    average_waiting_time = waiting_time / len(processes)
    print(f"Priority Non-Preemptive Average Waiting Time: {average_waiting_time:.2f}")

def round_robin_preemptive(processes, time_quantum):
    queue = []
    current_time = 0
    waiting_time = 0
    remaining_processes = processes.copy()

    while remaining_processes or queue:
        for process in remaining_processes:
            if process[1] <= current_time:
                queue.append(process)
                remaining_processes.remove(process)

        if queue:
            process = queue.pop(0)
            waiting_time += max(0, current_time - process[1])  # Calculate waiting time
            execution_time = min(time_quantum, process[2])
            current_time += execution_time
            process[2] -= execution_time

            if process[2] > 0:
                queue.append(process)
        else:
            current_time += 1

    average_waiting_time = waiting_time / len(processes)
    print(f"Round Robin Preemptive (Time Quantum={time_quantum}) Average Waiting Time: {average_waiting_time:.2f}")


# Example processes (process_id, arrival_time, burst_time, priority)
processes = [
    [1, 0, 8, 3],
    [2, 1, 6, 2],
    [3, 2, 1, 1],
    [4, 3, 10, 4],
]

# Simulate scheduling algorithms
fcfs(processes)
sjf_preemptive(processes)
priority_non_preemptive(processes)
round_robin_preemptive(processes, time_quantum=2)