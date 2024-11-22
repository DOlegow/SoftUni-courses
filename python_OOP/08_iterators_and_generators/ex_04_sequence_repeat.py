class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration

        # Get the current character in the sequence
        current_char = self.sequence[self.index % len(self.sequence)]

        # Update the index and decrease the remaining number
        self.index += 1
        self.number -= 1

        return current_char

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
