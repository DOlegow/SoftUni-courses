number_of_snowballs = int(input())
highest_calculated_snowball_value = 0

for data in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value_of_snowball = (snowball_weight / snowball_time) ** snowball_quality
    if highest_calculated_snowball_value < value_of_snowball:
        highest_calculated_snowball_value = value_of_snowball
        max_snowball_weight = snowball_weight
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality
print(f"{max_snowball_weight} : {max_snowball_time} = {highest_calculated_snowball_value:.0f} ({max_snowball_quality})")
