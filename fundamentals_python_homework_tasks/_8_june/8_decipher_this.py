secret_message = input().split(' ')

digits = [digit for digit in range(10)]
list_of_letters = []
deciphered_message = []

for word in secret_message:
    digits_in_word = ''
    decipher_word = ''
    word_without_digits = ''
    for i in range(len(word)):
        if word[i] in str(digits):
            digits_in_word += word[i]
        else:
            word_without_digits += word[i]

    first_symbol = chr(int(digits_in_word))
    decipher_word = first_symbol + word_without_digits
    list_of_letters = [letter for letter in decipher_word]
    list_of_letters[1], list_of_letters[-1] = list_of_letters[-1], list_of_letters[1]
    decipher_word = "".join(list_of_letters)
    deciphered_message.append(decipher_word)
deciphered_words = " ".join(deciphered_message)
print(deciphered_words)
