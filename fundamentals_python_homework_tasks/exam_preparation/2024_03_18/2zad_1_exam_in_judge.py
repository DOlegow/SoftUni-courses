import re


def extract_food_info(input_string):
    pattern = r'(?:#([A-Za-z\s]+)#(\d{2}/\d{2}/\d{2})#(\d+)#)|(?:\|([A-Za-z\s]+)\|(\d{2}/\d{2}/\d{2})\|(\d+)\|)'
    matches = re.findall ( pattern, input_string )
    food_items = [match[:3] if match[0] else match[3:] for match in matches]
    return food_items


def calculate_days(total_calories):
    daily_calories_requirement = 2000
    days = total_calories / daily_calories_requirement
    return int ( days )


def main():
    input_string = input ().strip ()

    food_items = extract_food_info ( input_string )

    if not food_items:
        print ( "You have food to last you for: 0 days!" )
        return

    total_calories = 0
    valid_food_items = []

    for item, expiration_date, calories in food_items:
        total_calories += int ( calories )
        valid_food_items.append ( (item, expiration_date, calories) )

    if not valid_food_items:
        print ( "You have food to last you for: 0 days!" )
        return

    days = calculate_days ( total_calories )

    print ( f"You have food to last you for: {days} days!" )

    for item, expiration_date, calories in valid_food_items:
        print ( f"Item: {item.strip ()}, Best before: {expiration_date.strip ()}, Nutrition: {calories}" )


if __name__ == "__main__":
    main ()
