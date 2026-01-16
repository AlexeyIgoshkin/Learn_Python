original_list = [(1, 101), (101, 1)]  # Список кортежей

new_dict = {}
for key, value in original_list:  # Можем распаковать прямо в вызове цикле
	new_dict[key] = value  # и разложить в новый словарь
print('Через цикл for:', new_dict)

# new_dict = {x: x * 3 for x in original_list}
new_dict = {key: value for key, value in original_list}  # Распаковка через компрехеншн

print('Через list comprehension:', new_dict)

new_dict = dict(original_list)  # Еще проще. Встроенная функция dict все сама распарсит
print('Через парсинг dict:', new_dict)

original_keys = ['one', 'two', 'three']
original_values = [1, 2, 3]

united_dict = dict(zip(original_keys, original_values))
print(united_dict)
