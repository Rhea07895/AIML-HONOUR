#step 1 :create a profiling decorator to identify start and end time of the function 
# a function where you pass n that will run for 10 lakhs
#do similar calculations
#after running check the profiling and signature of the function


import time
import cProfile
import pstats
import inspect
from functools import wraps
from datetime import datetime

def calculate_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        print("Start time:", datetime.now())

        result = func(*args, **kwargs)

        end = time.perf_counter()
        print("End time:", datetime.now())
        print("Execution time:", end - start, "seconds")

        return result
    return wrapper

@calculate_time
def calculation(n):
    total = 0

    for i in range(n):
        total = total + i * i

    return total

print("Result:", calculation(1000000))

print("Function signature:", inspect.signature(calculation))

profiler = cProfile.Profile()
profiler.enable()

calculation(1000000)

profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats("cumulative")
stats.print_stats()