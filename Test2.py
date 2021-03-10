tuple1 = [(1, 2), (2, 3)]
for a, b in tuple1:
    print(a + b)

dictionary_test = {
    'wolf': 100,
    'hamster': 200,
    'monkey': 30,
    'bird': 1,
}

total_mass = 0
for animal, mass in dictionary_test.items():
    print(animal, mass)
    total_mass += mass
for mass in dictionary_test.values():
    print(mass)
print(total_mass)

mine_list_of_weather = ['warm', 'cold', 'hot', 'wind', 'sun', ]
for i, weather in enumerate(mine_list_of_weather):
    print(i, weather)
