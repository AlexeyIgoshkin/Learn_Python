# Любая инструкция if выполняет выражение, которое автоматически конвертируется в bool
# Порядок следования условий важен. if-elif-else - зависимые условия

num_one = 6
num_two = 6.2

if (num_one > 0 and  # Условие с операторами and. Выполняется, если типы в переменных правильные и > 0
		num_two > 0 and
		isinstance(num_one, int) and  # if type(num_one) is int - вариант написания
		isinstance(num_two, float)):
	print("Yes, it is")
else:
	print("No, it isn't")

my_phone = {
	'brand': 'iPhone',
	'price': 200,
	'storage': '256GB'
}

if not my_phone.get('storage'):  # Проверяем, что ключа storage нет
	print("No 'storage' key in it")
else:
	print("There is 'storage' key, value:", my_phone['storage'])


def numbers(a, b):  # Проверка, что все типы - int
	if not isinstance(a, int) or not isinstance(b, int):
		return "One of the arguments is not int-type. Closing..."
	if a >= b:
		return f"{a} larger or even to {b}"
	return f"{b} larger than {a}"


print()
print(numbers(5.2, 2))
print(numbers(3, 5))
print(numbers("2d2dada", True))

correct_dict1 = {'distance': 245}

correct_dict2 = {
	'speed': 24,
	'time': 12,
}

incorrect_dict = {
	'potato': 'brown',
	'class': 'vegetables',
}

print()


def route_info(some_dict: dict):  # Проверяем словарь на наличие полей
	if 'distance' in some_dict and isinstance(some_dict['distance'], int):
		route = f"Distance to your destination is {some_dict['distance']}"
	elif (some_dict.get('speed')) and (type(some_dict['speed']) is int) and ('time' in some_dict):
		route = f"Distance to your destination is calculated as {some_dict['speed'] * some_dict['time']}"
	else:
		route = "No distance info is available"
	return print(route)


route_info(correct_dict1)
route_info(correct_dict2)
route_info(incorrect_dict)

# Забавный факт:
print(incorrect_dict.get('potato'))
print(incorrect_dict['potato'])
# Одно и тоже, почти
