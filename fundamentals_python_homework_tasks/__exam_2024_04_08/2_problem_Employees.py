import re

number = int(input())
for n in range(number):
    text = input()
    pattern = '([A-Z]{1}[a-z]{2,} [A-Z][a-z]{2,})#+(([A-Z][a-z]+)&?([A-Z][a-z]+)&?([A-Z][a-z]+)?)\d{2}([A-Z][A-Za-z0-9]+ (JSC|Ltd.))'
    matches = re.search(pattern, text)
    if matches:
        employee_name = matches.group(1)
        job_position = matches.group(3)+ ' ' + matches.group(4)
        company_name = matches.group(6)
        print(f"{employee_name} is {job_position} at {company_name}")
