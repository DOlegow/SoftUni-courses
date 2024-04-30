import math

def heart_pattern():
    for x in range(25, -25, -1):
        line = ''
        for y in range(-50, 50):
            if (((y * 0.04) ** 2 + (x * 0.1) ** 2 - 1) ** 3 - (y * 0.04) ** 2 * (x * 0.1) ** 3) <= 0:
                line += '*'
            else:
                line += ' '

        print(line)

heart_pattern()
