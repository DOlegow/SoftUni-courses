def number_increment(numbers):
    def increase():
        # Increment each number in the list
        for i in range(len(numbers)):
            numbers[i] += 1
    increase()  # Call the increase function to modify the list
    return numbers


print(number_increment([1, 2, 3]))
