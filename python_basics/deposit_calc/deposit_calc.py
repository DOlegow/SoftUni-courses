deposit = float(input())
srok = int(input())
annual_percent = float(input())
sum_deposit = deposit + srok*((deposit*annual_percent/100)/12)
print(sum_deposit)