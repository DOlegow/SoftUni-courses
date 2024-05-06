def count_beach_words(string):
    word_count = 0
    string = string.lower()
    words_to_count = ["sand", "water", "fish", "sun"]
    for word in words_to_count:
        word_count += string.count(word.lower())
    return word_count

input_string = input()
count = count_beach_words(input_string)
print(count)