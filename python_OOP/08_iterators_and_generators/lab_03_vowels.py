class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0
        self.vowel_list = 'aeiouyAEIOU'

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            ch = self.string[self.index]
            self.index += 1
            if ch in self.vowel_list:
                return ch
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
