stores = {}
important_items = set()  # Change important_items to a set to ensure uniqueness of items

def add_item(store, items):
    if store not in stores:
        stores[store] = []
    for item in items:
        if item not in stores[store] and item not in important_items:
            stores[store].append(item)
            important_items.add(item)  # Add the item to the set of important items

def add_important_item(store, item):
    if store not in stores:
        stores[store] = []
    if item not in stores[store]:
        stores[store].insert(0, item)
        important_items.add(item)  # Add the item to the set of important items

def remove_store(store):
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
            if any(item in stores[store] for item in important_items):
                continue  # Ignore removal if there are important items
            remove_store(store)
    elif command[0] == "Go Shopping":
        print_stores()
        break
