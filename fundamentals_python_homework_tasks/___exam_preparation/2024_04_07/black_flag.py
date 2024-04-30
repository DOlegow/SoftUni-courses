days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
plunder = 0

for day in range(1, days+1):
    plunder += daily_plunder
    if day % 3 == 0:
        plunder += daily_plunder / 2
    if day % 5 == 0:
        plunder -= plunder*0.3

if plunder >= expected_plunder:
    print(f"Ahoy! {plunder:.2f} plunder gained.")
elif plunder < expected_plunder:
    percentage = plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
