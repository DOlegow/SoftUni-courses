def multiply(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * times
        return wrapper
    return decorator


# Test Code
@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))  # Output: 39


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))  # Output: 80
