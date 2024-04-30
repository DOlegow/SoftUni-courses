n=int(input())
p1=0
p2=0
p3=0
p4=0
p5=0
p1_sum=0
p2_sum=0
p3_sum=0
p4_sum=0
p5_sum=0

for i in range(0,n):
    num=int(input())
    if num < 200:
       p1_sum+=1
    elif num <=399:
       p2_sum +=1
    elif num <= 599:
       p3_sum+=1
    elif num <= 799:
       p4_sum+=1
    elif num >= 800:
       p5_sum+=1
p1=p1_sum/n*100
p2=p2_sum/n*100
p3=p3_sum/n*100
p4=p4_sum/n*100
p5=p5_sum/n*100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')