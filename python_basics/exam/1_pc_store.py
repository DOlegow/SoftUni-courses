proc_price = float(input())
video_price = float(input())
ram_price = float(input())
count_ram = int(input())
discount = float(input())

proc_price_lv = proc_price * 1.57
video_price_lv = video_price * 1.57
ram_price_lv = ram_price * 1.57
price_ram = ram_price_lv * count_ram
cpu_with_discount = proc_price_lv - proc_price_lv * discount
video_with_discount = video_price_lv - video_price_lv * discount
total_price = cpu_with_discount + video_with_discount + price_ram

print(f'Money needed - {total_price:.2f} leva.')