stores = {}

def add_item(store, items):
    global stores
    if store not in stores:
        stores[store] = []
    items_in_other_stores = {item for other_store, other_items in stores.items() if other_store != store for item in other_items}
    for item in items:
        if item not in items_in_other_stores:
            stores[store].append(item)

def add_important_item(store, item):
    global stores
    if store not in stores:
        stores[store] = []
    if item not in {item for sublist in stores.values() for item in sublist}:
        stores[store].insert(0, item)

def remove_store(store):
    global stores
    if store in stores:
        del stores[store]

def print_stores():
    for store, items in stores.items():
        print(f"{store}:")
        for item in items:
            print(f" - {item}")

while True:
    command = input().split("->")
    if command[0] == "Add":
        store = command[1]
        items = command[2].split(",")
        add_item(store, items)
    elif command[0] == "Important":
        store = command[1]
        item = command[2]
        add_important_item(store, item)
    elif command[0] == "Remove":
        store = command[1]
        if store in stores:
            remove_store(store)
    elif command[0] == "Go Shopping":
        print_stores()
        break
