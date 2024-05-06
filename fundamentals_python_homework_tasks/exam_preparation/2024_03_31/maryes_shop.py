stock = {}
sold_total = 0

while True:
    command = input()
    if command == "Complete":
        break

    action, quantity, food = command.split ()
    quantity = int ( quantity )

    if quantity <= 0:
        break

    if action == "Receive":
        stock[food] = stock.get ( food, 0 ) + quantity
    elif action == "Sell":
        if food not in stock:
            print ( f"You do not have any {food}." )
        elif stock[food] < quantity:
            sold_quantity = stock[food]
            sold_total += sold_quantity
            del stock[food]
            print ( f"There aren't enough {food}. You sold the last {sold_quantity} of them." )

        else:
            stock[food] -= quantity
            sold_total += quantity
            print ( f"You sold {quantity} {food}." )



for food, quantity in stock.items():
    if quantity > 0:
        print(f"{food}: {quantity}")


print(f"All sold: {sold_total} goods")

