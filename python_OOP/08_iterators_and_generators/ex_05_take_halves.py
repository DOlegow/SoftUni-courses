def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for num in integers():
            yield num / 2

    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result

    return take, halves, integers


# Example usage:
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))  # Output: [0.5, 1.0, 1.5, 2.0, 2.5]
print(take(0, halves()))  # Output: []
