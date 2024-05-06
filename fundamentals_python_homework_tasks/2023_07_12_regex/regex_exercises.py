import re

text = input()
pattern = "\b\d{1,2}-[A-Z][a-z]{2}-\d{4}\b"
result = re.findall(pattern, text)

print(result)
