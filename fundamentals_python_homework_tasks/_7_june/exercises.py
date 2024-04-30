x = [num for num in range(5)]
print(x)
squares = [y**2 for y in x]
print(squares)
evens = [num for num in x if num % 2 == 0]
print(evens)
filtered = [True if k % 2 == 0 else False for k in x]
print(filtered)

text = input()
vowels = ['a', 'u', 'o', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
no_vowels = ''.join([f for f in text if f not in vowels])
print(no_vowels)
