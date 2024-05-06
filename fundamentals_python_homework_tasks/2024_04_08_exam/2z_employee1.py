import re
def is_valid_employee(name, job, company):
    if not re.match(r'^[A-Z][a-z]{2,}\s[A-Z][a-z]{2,}[A-Z][a-zA-Z&]+(#([A-Z][a-zA-Z&]+)){0,2}\d{2}[A-Za-z]+\s(JSC|Ltd\.)$', name):
        return False
    return True
def decrypt_input(num_inputs, inputs):
    for i in range(num_inputs):
        data = inputs[i].split('#')
        if len(data) != 3:
            continue
        name, job, company = data
        if is_valid_employee(name, job, company):
            name_parts = name.split()
            employee_name = ' '.join([part.capitalize() for part in name_parts])
            job_parts = job.split('#')[1].split('&')
            job_position = ' '.join([part.capitalize() for part in job_parts])
            company_info = company.split()
            company_name = ' '.join([part.capitalize() for part in company_info[:-1]])
            company_type = company_info[-1]
            print(f"{employee_name} is {job_position} at {company_name} {company_type}")
num_inputs = int(input())
decrypt_input(num_inputs, inputs)