morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}

def morse_to_english(morse_code):
    words = morse_code.split(' | ')
    english_message = []
    for word in words:
        letters = word.split()
        english_word = ''
        for letter in letters:
            english_word += morse_code_dict.get(letter, '')
        english_message.append(english_word)
    return ' '.join(english_message)
morse_message = input()
english_translation = morse_to_english(morse_message)
print(english_translation)
