#11.create decorator function to measure execution time of function

import time

def example_function(n):
    time.sleep(n)
start_time = time.time()
example_function(2)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")