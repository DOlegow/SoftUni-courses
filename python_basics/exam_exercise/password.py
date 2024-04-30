import string
import random

signs = string.ascii_letters + string.digits + string.punctuation
lenght = 8
current_password = ''.join(random.sample(signs, lenght))

print(current_password)

