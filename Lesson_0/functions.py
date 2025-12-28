# создать функцию с двумя листами, объединить в словарь, вернуть его из функции и распечатать
def separator():
	return print('-' * 50)


def merge_lists_do_dict(list_one: list, list_two: list):
	#united_lists = dict(zip(list_one, list_two))
	#return united_lists
	return dict(zip(list_one, list_two)) # а можно вот так ебануть


dictionary_one = merge_lists_do_dict([1, 2, 3], ['one', 'two', 'three'])
dictionary_two = merge_lists_do_dict([(), 'True', False], [(1,3,5), {2, 4}, {1: 45}])
dictionary_named_args = merge_lists_do_dict([True, False, 2], list_two=['Da', 'Net', 7])

print(dictionary_one)
print(dictionary_two)
print(dictionary_named_args)

separator()

# Функция с резиновыми аргументами
def infinity_arguments(*args):
	return sum(args)

args_sum = infinity_arguments(2, 5, 144, 5125, 52)
print(args_sum)

# Функция с аргументами в качестве словаря (по сути он бесконечный, но при вызове нужны именованные параметры)
def dict_arguments(**canine):
	print(canine) # Сам словарь до парсинга
	return print(f"My dog's name is {canine['dog_name']}. "
				 f"It's {canine['dog_age']}. "
				 f"He is my {canine['is_true']} family member!")

dict_arguments(dog_name='Charlie', dog_age=3, is_true=True, dog_color='Brown')

separator()

# Разделяю ключи и значение внутри функции, которая имеет параметры словаря и строки.
# Если строка содержит название любого ключа словаря, то печатаем все ключи словаря.
# Если не содержит - печатаем все значения словаря. Да, логика ебанутая, но она есть))
def dict_separation(example_dict: dict, string: str):
	dict_keys_list = example_dict.keys()
	dict_values_list = example_dict.values()
	if string in example_dict.keys():
		print(dict_keys_list)
	else:
		print(dict_values_list)


dict_separation({'dog_name':'Charlie', 'dog_age': 3, 'is_true': True, 'dog_color': 'Brown'},
				'is_true')

separator()


# Функция с именоваными аргументами
def named_func(name, age):
	return print(f"Hello, {name}, I know that you are {age}")

named_func(age=35, name='Alex') # Круто, указаны имена аргументам, код более читаем
named_func(35, 'Alex') # Не круто, порядок нарушен
named_func('Alex', age=35) # Комбинить позиционный и именованый аргументы можно, но зачем?

separator()


def update_car_info(**car):
	car['is_available'] = True
	return car


car_update_result = update_car_info(brand='Toyota', price=30000)
print(car_update_result)