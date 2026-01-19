my_dict = {1: 'one', 2: 'two', '42': 2}

# Распечатать ключи и значения можно следующими способами:
for key in my_dict:
	print(key, my_dict[key])  # Вызываем через ключ, выдирание значения по этому ключу

for k, v in my_dict.items():  # ВЫзываем ключ и значение сразу через метод .items()
	print(k, v)
	print(type(k), type(v))


# Задача №1
def dict_to_list(some_dict: dict):
	# return list(some_dict) ---- можно сразу так, если нет доп условий
	result = []
	for key, value in some_dict.items():
		if isinstance(key, int):
			key *= 2
		result.append((key, value))
	return result


print(dict_to_list(my_dict))

# Задача №2
great_list = [1, 2, 'text', True, {4, 5}, [4, 7], ('apple', 'banana'), {'key': 'value'}]


def filter_list(some_list: list, typo: type) -> list:
	result = []
	for el in some_list:
		if type(el) is typo:
			result.append(el)
	return result


# Та же функция с list comprehension:
def filter_list2(some_list: list, typo: type) -> list:
	return [el for el in some_list if type(el) is typo]


# Та же функция с lambda filter:
def filter_list3(some_list: list, typo: type) -> list:
	return list(filter(lambda x: type(x) == typo, some_list))


print(filter_list(great_list, int))
print(filter_list(great_list, str))
print(filter_list(great_list, bool))
print(filter_list(great_list, tuple))
print(filter_list(great_list, dict))
print(filter_list(great_list, list))
print(filter_list(great_list, set))

print(filter_list2(great_list, int))
print(filter_list2(great_list, str))
print(filter_list2(great_list, bool))
print(filter_list2(great_list, tuple))
print(filter_list2(great_list, dict))
print(filter_list2(great_list, list))
print(filter_list2(great_list, set))

print(filter_list3(great_list, int))
print(filter_list3(great_list, str))
print(filter_list3(great_list, bool))
print(filter_list3(great_list, tuple))
print(filter_list3(great_list, dict))
print(filter_list3(great_list, list))
print(filter_list3(great_list, set))
