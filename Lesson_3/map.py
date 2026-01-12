my_list = [2, 5, 6, 21, 5, 234, 2]


def numbers_multi(number) -> int:
	return number * 2


map_list = map(numbers_multi, my_list)  # map здесь принимает функцию и список.
# То есть что нужно сделать и с чем

lambda_list = tuple(map(lambda num: num * 2, my_list))  # через Лямбду тоже самое,
# но гораздо проще (тут преобразуем сразу в кортеж)


print(my_list)
print(lambda_list)
print(list(map_list))

x_set = {2, 15, 5, 3, 1, 30, 45, 52, 67, 8, 312, 90, 14, 56, 2, 6}  # Возьмем набор (редко берем)


def three_five_matching(some_set: set):  # Есть вот такая функция с условиями
	edited_set = set()
	for x in some_set:
		if x % 3 == 0 and x % 5 == 0:
			edited_set.add(x * 15)
		else:
			edited_set.add(x * 2)
	return edited_set


print(three_five_matching(x_set))

# А есть вот такой пиздец с лямбдой и тернарником. Одно и то же
# Так, конечно, кода меньше, но понять сложнее, поэтому не пользуйся длинными выражениями, Леха
# Потом скажешь себе спасибо
fiz_buzz_list = map(lambda x: f'3/5 Match! Result: {x * 15}' if x % 3 == 0 and x % 5 == 0 else f'Sqr: {x * 2}', x_set)
print(list(fiz_buzz_list))
# "Ну что это за пиздец? Ну как это может быть в 21 веке?" ©
