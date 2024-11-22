def type_check(expected_type):
    def decorator(func):
        def wrapper(arg):
            if isinstance(arg, expected_type):
                return func(arg)
            else:
                return "Bad Type"
        return wrapper
    return decorator

# Test Code
@type_check(int)
def times2(num):
    return num * 2

print(times2(2))  # Output: 4
print(times2('Not A Number'))  # Output: Bad Type

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))  # Output: H
print(first_letter(['Not', 'A', 'String']))  # Output: Bad Type
