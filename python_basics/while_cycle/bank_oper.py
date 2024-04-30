n = input()
balance = 0.0
while n != "NoMoreMoney":
    amount = float(n)
    if amount < 0:
        print("Invalid operation!")
        break
    balance += amount
    print(f"Increase: {amount:.2f}")
    n = input()

print(f"Total: {balance:.2f}")
