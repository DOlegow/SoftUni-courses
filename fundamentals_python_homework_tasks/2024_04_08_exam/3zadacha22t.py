def add_item(store, items, stores):
    if store in stores:
        for item in items:
            if item not in stores[store]:
                stores[store].append(item)
    else:
        stores[store] = items

def add_important_item(store, item, stores):
    if store in stores:
        if item not in stores[store]:
            important_items.append(item)
            stores[store].insert(0, item)
    else:
        stores[store] = item

def remove_store(store, stores):
    if store in stores:
        for el in store:
            if el not in important_items:
                del stores[store]

if __name__ == "__main__":
    stores = {}

    command = input()
    important_items = []
    while command != "Go Shopping":
        command_parts = command.split("->")
        action = command_parts[0]

        if action == "Add":
            store = command_parts[1]
            items = [item.strip() for item in command_parts[2].split(",")]
            add_item(store, items, stores)
        elif action == "Important":
            store = command_parts[1]
            item = command_parts[2].strip()
            add_important_item(store, item, stores)
        elif action == "Remove":
            store = command_parts[1]
            remove_store(store, stores)

        command = input()

    for store, items in sorted(stores.items()):
        print(f"{store}:")
        for item in items:
            print(f" - {item}")
