class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise ValueError("Only strings can be added to the stack.")
        self.data.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"


# Example usage:
stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")
print(stack)  # Output: [{cherry}, {banana}, {apple}]
print(stack.top())  # Output: cherry
print(stack.pop())  # Output: cherry
print(stack.is_empty())  # Output: False
