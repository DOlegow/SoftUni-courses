import re

def is_mirror_word(word):
    return word == word[::-1]

def find_hidden_word_pairs(text):
    pattern = r'[@#]([A-Za-z]{3,})[@#]{2}([A-Za-z]{3,})[@#]'
    return re.findall(pattern, text)

def main():
    input_text = input()
    hidden_word_pairs = []
    match = find_hidden_word_pairs(input_text)
    for
    hidden_word_pairs.append(find_hidden_word_pairs(input_text))

    if not hidden_word_pairs:
        print("No word pairs found!")
        return

    mirror_word_pairs = [pair for pair in hidden_word_pairs if is_mirror_word(pair[0]) and is_mirror_word(pair[1])]

    if not mirror_word_pairs:
        print("No mirror words!")
    else:
        print(f"{len(mirror_word_pairs)} word pairs found!")
        print("The mirror words are:")
        for pair in range(0, len(mirror_word_pairs), 2):
            mirror_words = ", ".join(f"{mirror_word_pairs[pair]} <=> {mirror_word_pairs[pair + 1]}")
            print(mirror_words)

main()
