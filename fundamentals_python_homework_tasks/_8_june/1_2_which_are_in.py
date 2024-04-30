first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = [first_word for first_word in first_sequence
              if any(first_word in second_word for second_word in second_sequence)]
print(substrings)