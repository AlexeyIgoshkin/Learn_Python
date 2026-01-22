original_dict = {
	'a': 10,
	'b': 20,
	'c': 30
}

for_in_dict = {}
for key, value in original_dict.items():
	for_in_dict[key] = value * value

dict_comprehension = {key: value * value for key, value in original_dict.items()}
# Так не делается, но технически можно:
dict_lambda = dict(map(lambda item: (item[0], item[1] * item[1]), original_dict.items()))

print(for_in_dict)
print(dict_comprehension)
print(dict_lambda)

# Как напихать листом словарь, где ключи - индексы, а значения - значения в листе
list_to_dict = [10, 30, 20]

# Enumerate возвращает индекс и значение итерации, то есть список кортежей
dict_from_list = {key: value for key, value in enumerate(list_to_dict)}
print(dict_from_list)

# Задания:
str_dict = {'string1': 1, 'string2': 2, 'string3': 3}

str_dict_upper_modified = {key.upper(): value for key, value in str_dict.items()}
print(str_dict_upper_modified)

str_list_len = ['One', 'Two', 'Three', 'Four', 'Five']
str_list_len_modified = [x for x in str_list_len if len(x) > 3]

print(str_list_len_modified)
