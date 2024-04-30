journal_with_materials = input().split(", ")

command = input()

while True:
    if command == "Craft!":
        break
    tokens = command.split(" - ")
    what_to_do = tokens[0]
    material = tokens[1]

    if what_to_do == "Collect":
        if material not in journal_with_materials:
            journal_with_materials.append(material)

    elif what_to_do == "Drop":
        if material in journal_with_materials:
            journal_with_materials.remove(material)

    elif what_to_do == "Combine Items":
        old_item, new_item = material.split(":")
        if old_item in journal_with_materials:
            index = journal_with_materials.index(old_item)
            journal_with_materials.insert(index + 1, new_item)

    elif what_to_do == "Renew":
        if material in journal_with_materials:
            journal_with_materials.remove(material)
            journal_with_materials.append(material)

    command = input()

print(", ".join(journal_with_materials))
