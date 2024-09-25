from Threading import *

def add(x, y):
    time.sleep(1)  
    return x + y

def subtract(x, y):
    time.sleep(1)
    return x - y

def multiply(x, y):
    time.sleep(1)
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    time.sleep(1)
    return x / y

def threadedCalculations(operations):
    threads = []
    start_time = time.time()
    for op in operations:
        func, args = op
        t = run_in_thread(func, *args)
        threads.append(t)
    for t in threads:
        t.join()

    end_time = time.time()
    print(f"Time taken for parallel calculations: {end_time - start_time} seconds")

def simpleCalculations(operations):
    start_time = time.time()
    for op in operations:
        func, args = op
        result = func(*args)
        print(f"Result of {func.__name__}({args}): {result}")

    end_time = time.time()
    print(f"Time taken for non-parallel calculations: {end_time - start_time} seconds")

