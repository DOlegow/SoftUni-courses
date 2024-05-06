import re

number = int(input())
for n in range(number):
    text = input()
    pattern = r'^([A-Z][a-z]{2,}\s[A-Z][a-z]{2,})#+((?:[A-Z][a-z]+(?:&[A-Z][a-z]+)*)?)\d{2}([A-Za-z0-9]+\s(?:JSC|Ltd\.))$'
    matches = re.match(pattern, text)
    if matches:
        employee_name = matches.group(1)
        job_position = ' '.join(matches.group(2).split('&')).title()
        company_name = matches.group(3).title().replace('Jsc', 'JSC')
        print(f"{employee_name} is {job_position} at {company_name}")
