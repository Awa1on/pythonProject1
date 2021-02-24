print('Hello world!')
a = 21
b = 22
c = 31
d = 12
car = "Audi TT"
car.isalpha()

# Работа со списками
my_list = [1, 2, 3, 'Sad', 4, 5]
my_list.insert(3, "Max")
print(my_list)
another_list = [11, 12, 13]
my_list.extend(another_list)
print(my_list)
del my_list[2]
print(my_list)
my_list.remove(2)
print(my_list)
list_1 = [1, 2, 3]
list_2 = [3, 2]
print(list_1 > list_2)

if 5 in my_list:
    print(True)

list_3 = list(range(1, 10, 2))

print(list_3)
del my_list[1]
del my_list[1]

my_list.extend([22, 1, 5])
my_list.sort()
print(my_list)

my_dict = dict()
my_dict['Elf'] = "Legalas"
my_dict['Orc'] = 'Saruman'

if "Elf" in my_dict:
    print(my_dict)

my_dict.get("cat", 'Vasa')
my_dict.setdefault('cat', 'Barsik')
print(my_dict)
