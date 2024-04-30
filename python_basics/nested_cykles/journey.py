destination = input()
sm = 0
m = 0
while destination != "End":
    money = float(input())
    while sm < money:
        m = float(input())
        sm += m
    print(f'Going to {destination}!')
    sm = 0
    destination = input()