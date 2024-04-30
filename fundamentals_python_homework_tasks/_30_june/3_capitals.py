country_names = input().split(', ')
capital_cities = input().split(', ')
country_dict = {country_names[index]: capital_cities[index] for index in range(len(capital_cities))}
for country_names, capital_cities in country_dict.items():
    print(f'{country_names} -> {capital_cities}')

