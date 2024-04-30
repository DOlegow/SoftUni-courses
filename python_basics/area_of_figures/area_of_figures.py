from math import pi
figure = str(input())
if figure == "square":
    a = float(input())
    area = a*a
    print(f"{round(area,3):.3f}")
elif figure == "rectangle":
    a,b = float(input()),float(input())
    area = a*b
    print(f"{round(area,3):.3f}")
elif figure == "circle":
    r = float(input())
    area = pi*r**2
    print(f"{round(area,3):.3f}")
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = a*h/2
    print(f"{round(area,3):.3f}")

