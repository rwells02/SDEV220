
import multiprocessing
import time
import random
from datetime import datetime

def print_time_after_delay():
    wait_time = random.uniform(0, 1)  # Random float between 0 and 1
    time.sleep(wait_time)
    print(f"Process {multiprocessing.current_process().name} - Time: {datetime.now().strftime('%H:%M:%S.%f')}")

if __name__ == "__main__":
    processes = []

    # Create and start three processes
    for i in range(3):
        p = multiprocessing.Process(target=print_time_after_delay, name=f"Process-{i+1}")
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

