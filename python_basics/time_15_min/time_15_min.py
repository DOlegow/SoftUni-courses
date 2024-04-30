hour = int(input())
min = int(input())

if 0 <= hour < 24 and 0 <= min < 60:
    minutes = hour * 60 + min + 15
hours_after15m = minutes // 60
if hours_after15m == 24:
    hours_after15m = 0
minutes_after15m = minutes % 60
if minutes_after15m < 10:
   print(f'{hours_after15m}:0{minutes_after15m}')
else:
    print(f'{hours_after15m}:{minutes_after15m}')
