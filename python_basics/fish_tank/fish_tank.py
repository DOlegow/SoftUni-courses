lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())
vollume = lenght * width * height*0.001
vollume_l = vollume/1000
buzy = vollume/100*percent
necessary_l = vollume-buzy
print(necessary_l)

