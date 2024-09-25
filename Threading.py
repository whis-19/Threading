from Imports import *

def thread_function(func, *args, **kwargs):
    print(f"Thread initialized for {func.__name__} with arguments: {args} {kwargs}")
    result = func(*args, **kwargs)
    print(f"Thread for {func.__name__} has finished. Result: {result}")

def run_in_thread(func, *args, **kwargs):
    thread = threading.Thread(target=thread_function, args=(func,) + args, kwargs=kwargs)
    thread.start()
    return thread
