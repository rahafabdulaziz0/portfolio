# TASK 2  
import random
import numpy as np
import matplotlib.pyplot as plt

MEAN_INTERARRIVAL = 4.0
MEAN_SERVICE_ABL = 3.0
MEAN_SERVICE_BAK = 0.9
N_CUSTOMERS = 700
N_TRIALS = 100

def simulate_double_server():
    clock = 0.0
    next_arrival = random.expovariate(1 / MEAN_INTERARRIVAL)
    service_end_able = float('inf')
    service_end_bak = float('inf')
    waiting_times, service_times, time_in_system = [], [], []
    idle_time, last_event_time = 0.0, 0.0
    queue = []

    while len(waiting_times) < N_CUSTOMERS:
        next_event = min(next_arrival, service_end_able, service_end_bak)
        clock = next_event
        if service_end_able == float('inf') and service_end_bak == float('inf'):
            idle_time += clock - last_event_time
        last_event_time = clock

        if next_event == next_arrival:
            queue.append(clock)
            next_arrival = clock + random.expovariate(1 / MEAN_INTERARRIVAL)
            if service_end_able == float('inf'):
                start = queue.pop(0)
                service_time = random.expovariate(1 / MEAN_SERVICE_ABL)
                service_end_able = clock + service_time
                waiting_times.append(clock - start)
                service_times.append(service_time)
                time_in_system.append(service_time + (clock - start))
            elif service_end_bak == float('inf'):
                start = queue.pop(0)
                service_time = random.expovariate(1 / MEAN_SERVICE_BAK)
                service_end_bak = clock + service_time
                waiting_times.append(clock - start)
                service_times.append(service_time)
                time_in_system.append(service_time + (clock - start))

        elif next_event == service_end_able:
            if queue:
                start = queue.pop(0)
                service_time = random.expovariate(1 / MEAN_SERVICE_ABL)
                service_end_able = clock + service_time
                waiting_times.append(clock - start)
                service_times.append(service_time)
                time_in_system.append(service_time + (clock - start))
            else:
                service_end_able = float('inf')

        else:
            if queue:
                start = queue.pop(0)
                service_time = random.expovariate(1 / MEAN_SERVICE_BAK)
                service_end_bak = clock + service_time
                waiting_times.append(clock - start)
                service_times.append(service_time)
                time_in_system.append(service_time + (clock - start))
            else:
                service_end_bak = float('inf')

    avg_wait = np.mean(waiting_times)
    prob_wait = np.sum(np.array(waiting_times) > 0) / len(waiting_times)
    prob_idle = idle_time / clock
    avg_service = np.mean(service_times)
    avg_arrival = MEAN_INTERARRIVAL
    avg_wait_for_waiters = np.mean([w for w in waiting_times if w > 0]) if prob_wait > 0 else 0
    avg_system = np.mean(time_in_system)

    return avg_wait, prob_wait, prob_idle, avg_service, avg_arrival, avg_wait_for_waiters, avg_system

results = [simulate_double_server() for _ in range(N_TRIALS)]
avg_results = np.mean(results, axis=0)

print("\n--- Final Results (Averaged across 100 Trials) ---")
labels = [
    "Average waiting time",
    "Probability that a customer has to wait",
    "Probability of idle server",
    "Average service time",
    "Average time between arrivals",
    "Average waiting time (for those who wait)",
    "Average time customer spends in the system"
]

for i, label in enumerate(labels):
    print(f"{i+1}. {label}: {avg_results[i]:.4f}")

choice = random.randint(0, 6)
data = [r[choice] for r in results]
plt.figure(facecolor='white')
plt.hist(data, bins=15, color='skyblue', edgecolor='black', alpha=0.8)
plt.axvline(np.mean(data), color='red', linestyle='--', linewidth=2, label=f"Mean: {np.mean(data):.4f}")
plt.title(f"Histogram for {labels[choice]} (100 Trials)")
plt.xlabel("Value")
plt.ylabel("Frequency (Number of Trials)")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
