def print_cities(cities, num, str="I have visited the city of "):
    for city in cities[:num]:
        print(f'{str} {city}')

city_list = ["Middletown", "Cullman", "Nashville", "Denver", "LA"]

print_cities(city_list, 5)
print_cities(city_list, 1, "My mother grew up in ")

