#11.create decorator function to measure execution time of function

import time
def decorator(func):
    def wrap(*args, **kwargs):
        start_time = time.time()  
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        end_time = time.time()  
        time_taken = end_time - start_time  
        print(f"Function {func.__name__} executed in {time_taken:.4f} seconds.")
        return result
    return wrap

@decorator
def multiply_numbers(x, y):
    return x * y

p=decorator(multiply_numbers)
p(10, 20) 
