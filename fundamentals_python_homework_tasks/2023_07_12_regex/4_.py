import re

string = 'There are 3 dogs and 4 cats'
result = re.sub('\d', 'GOSHO', string)

print(result)

text = 'Hello World'

print(re.findall('hello', text))

print(re.findall('hello', text, re.IGNORECASE))

text = '''start one
