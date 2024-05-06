stores = {}

def add_item(store, items):
    if store not in stores:
        stores[store] = []
    for item in items:
        if item not in stores[store]:
            stores[store].append(item)

def add_important_item(store, item):
    if store not in stores:
        stores[store] = []
    if item not in stores[store]:
        important_items.append(item)
        stores[store].insert(0, item)

def remove_store(store):
    if store in stores:
        del stores[store]

def print_stores():
    for store, items in stores.items():
        print(f"{store}:")
        for item in items:
            print(f" - {item}")
important_items = []
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
        for el in important_items:
            if el not in stores.items():
                remove_store(store)
    elif command[0] == "Go Shopping":
        print_stores()
        break