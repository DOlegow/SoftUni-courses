speed = float(input())
if speed <= 10:
    print('slow')
if 10 < speed <= 50:
    print('average')
if 50 < speed <= 150:
    print('fast')
if 150 < speed <= 1000:
    print('ultra fast')
if speed > 1000:
    print('extremely fast')
