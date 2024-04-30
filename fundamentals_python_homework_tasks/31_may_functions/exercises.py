


def sum_numbers(value_a: int, value_b: int) -> int:
    return value_a + value_b


while True:
    a = int(input('Enter a value for "A": '))
    b = int(input('Enter a value for "B": '))
    result = sum_numbers(a, b)
    print(result)
