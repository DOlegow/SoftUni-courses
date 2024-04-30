import re

names = input()
pattern = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"

matches = re.findall(pattern, names)
print(matches)
for name in matches:
    print(name, end=' ')
 #   Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett