annual_fee = int(input())
sneakers = annual_fee - annual_fee/100*40
suit = sneakers - sneakers/100*20
ball = suit/4
accessories = ball/5
total = annual_fee + sneakers + suit + ball + accessories
print(total)

