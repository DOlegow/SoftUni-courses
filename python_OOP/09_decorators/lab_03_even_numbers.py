def even_numbers(function):
    def wrapper(numbers):
        # Filter the even numbers
        even_nums = [num for num in numbers if num % 2 == 0]
        return function(even_nums)
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
