def apply_operations(activation_key, instructions):
    while True:
        instruction = input ().strip ()
        if instruction == "Generate":
            break
        instructions.append ( instruction )
    for instruction in instructions:
        if instruction.startswith("Slice"):
            _, start_index, end_index = instruction.split(">>>")
            start_index = int(start_index.strip())
            end_index = int(end_index.strip())
            activation_key = activation_key[:start_index] + activation_key[end_index:]
            print(activation_key)
        elif instruction.startswith("Flip"):
            _, case, start_index, end_index = instruction.split(">>>")
            start_index = int(start_index.strip())
            end_index = int(end_index.strip())
            if case == "Upper":
                activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() + activation_key[end_index:]
            elif case == "Lower":
                activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() + activation_key[end_index:]
            print(activation_key)
        elif instruction.startswith("Contains"):
            _, substring = instruction.split(">>>")
            substring = substring.strip()
            print(f"{activation_key} contains {substring}" if substring in activation_key else "Substring not found!")
    print ( f"Your activation key is: {activation_key}" )

act_key = input().strip()
instructions = []

apply_operations(act_key, instructions)
