key = int(input())
n = int(input())
decrypted_message = ''
for i in range (n):
    letter = input()
    decrypted_message += chr(ord(letter) + key)

print(decrypted_message)