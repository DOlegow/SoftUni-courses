def is_valid_name(name):
    parts = name.split()
    if len(parts) == 2:
        first_name, last_name = parts
        if first_name[0].isupper() and last_name[0].isupper() and len(first_name) >= 3 and len(last_name) >= 3:
            return True
    return False

def is_valid_position(position):
    parts = position.split("#")
    if len(parts) == 2:
        employee_part, company_part = parts
        if employee_part.count("&") <= 2 and all(word[0].isupper() for word in employee_part.split("&")):
            return True
    return False

def is_valid_company(company):
    parts = company.split()
    if len(parts) == 3:
        try:
            int(parts[1])  # Check if the middle part is a two-digit number
            if parts[0][0].isupper() and parts[2] in {"JSC", "Ltd."}:
                return True
        except ValueError:
            pass
    return False

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        info = input()
        name, position, company = info.split("##")
        if is_valid_name(name) and is_valid_position(position) and is_valid_company(company):
            employee_name = " ".join(name.split()).capitalize()
            job_position = " ".join(position.split("#")[0].split("&")).capitalize()
            company_name = " ".join(company.split()[:-1])
            print(f"{employee_name} is {job_position} at {company_name}")
