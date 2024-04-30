def decipher_message(message):
    words = message.split ()  # Разделяем сообщение на слова
    deciphered_words = []

    for word in words:
        code = int ( word[1:-1] )  # Получаем код символа из первых символов слова
        second_letter = word[1]  # Получаем вторую букву слова
        last_letter = word[-1]  # Получаем последнюю букву слова

        deciphered_word = chr ( code ) + last_letter + word[2:-1] + second_letter
        deciphered_words.append ( deciphered_word )

    deciphered_message = ' '.join ( deciphered_words )  # Объединяем расшифрованные слова обратно в сообщение
    return deciphered_message


# Пример использования:
secret_message = "72olle 103doo 100ya"
deciphered_message = decipher_message ( secret_message )
print ( deciphered_message )
