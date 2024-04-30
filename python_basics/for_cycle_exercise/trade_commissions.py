town = input()
s = float(input())
k = 0

if town == "Sofia":
    if 0 <= s <= 500:
        k = s * 0.05
        print(f'{k:.2f}')
    elif 500 < s <= 1000:
        k = s * 0.07
        print(f'{k:.2f}')
    elif 1000 < s <= 10000:
        k = s * 0.08
        print(f'{k:.2f}')
    elif s > 10000:
        k = s * 0.12
        print(f'{k:.2f}')
    else:
        print("error")
elif town == "Varna":
    if 0 <= s <= 500:
        k = s * 0.045
        print(f'{k:.2f}')
    elif 500 < s <= 1000:
        k = s * 0.075
        print(f'{k:.2f}')
    elif 1000 < s <= 10000:
        k = s * 0.1
        print(f'{k:.2f}')
    elif s > 10000:
        k = s * 0.13
        print(f'{k:.2f}')
    else:
        print("error")
elif town == "Plovdiv":
    if 0 <= s <= 500:
        k = s * 0.055
        print(f'{k:.2f}')
    elif 500 < s <= 1000:
        k = s * 0.08
        print(f'{k:.2f}')
    elif 1000 < s <= 10000:
        k = s * 0.12
        print(f'{k:.2f}')
    elif s > 10000:
        k = s * 0.145
        print(f'{k:.2f}')
    else:
        print("error")
else:
    print("error")
