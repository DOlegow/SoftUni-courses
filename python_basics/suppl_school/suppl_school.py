pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())
price = pens*5.80+markers*7.20+detergent*1.20
price_without_discount = price - (price/100*discount)
print(price_without_discount)
