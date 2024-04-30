bitcoin = int(input())
chinese_yuan = float(input())
commission = float(input())

bitcoin_lev = bitcoin * 1168
chinese_yuan_dollar = chinese_yuan * 0.15
chinese_yuan_lev = chinese_yuan_dollar * 1.76
euro = (bitcoin_lev + chinese_yuan_lev)/1.95
total = euro - euro * commission/100
print(f'{total:.2f}')
