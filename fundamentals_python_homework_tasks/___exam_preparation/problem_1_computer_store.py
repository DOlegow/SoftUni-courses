command = ''
total_price_without_taxes = 0
total_amount_of_taxes = 0
total_price_with_taxes = 0

while command != 'special' or command != 'regular':

    command = input()
    if command == 'special' or command == 'regular':
        break
    part_price = float(command)
    if part_price < 0:
        print('Invalid price!')
        continue
    total_price_without_taxes += part_price
    total_amount_of_taxes += part_price * 0.2
    total_price_with_taxes = total_price_without_taxes + total_amount_of_taxes
if total_price_without_taxes == 0:
    print('Invalid order!')
elif command == 'special':
    total_price_with_taxes = total_price_with_taxes - total_price_with_taxes * 0.1
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price_without_taxes:.2f}$')
    print(f'Taxes: {total_amount_of_taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price_with_taxes:.2f}$')
elif command == 'regular':
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price_without_taxes:.2f}$')
    print(f'Taxes: {total_amount_of_taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price_with_taxes:.2f}$')
