class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        else:
            item = self.iterable[self.index]
            self.index -= 1
            return item


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
