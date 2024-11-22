def cache(func):
    # Create a dictionary to store computed values
    log = {}

    def wrapper(n):
        # Check if the value is already computed
        if n not in log:
            # Compute and store the result in the log
            log[n] = func(n)
        return log[n]

    # Attach the log dictionary to the wrapper function
    wrapper.log = log
    return wrapper

# Define the recursive Fibonacci function
@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test examples
fibonacci(3)
print(fibonacci.log)  # {1: 1, 0: 0, 2: 1, 3: 2}
fibonacci(4)
print(fibonacci.log)  # {1: 1, 0: 0, 2: 1, 3: 2, 4: 3}
