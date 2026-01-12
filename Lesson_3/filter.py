original_list = [1, 3, 56, 62, 6, 23, 634, 6, 34, 634, 7, 3, 47, 2, 72, 7]


def even(x):  # Функция может вернуть результатом само сравнение, которое всегда является bool
	return x % 2 == 0

for number in original_list: # Через цикл вызываем функцию
	if even(number):
		print(f'{number}: Четное ({even(number)})')
	else:
		print(f'{number}: Нечетное ({even(number)})')

filtered_even_list = filter(lambda x: x % 2 == 0, original_list)  # Или фильтруем через лямбду even
filtered_odd_list = filter(lambda x: x % 2 != 0, original_list)  # Тут фильтруем odd
print(list(filtered_even_list))
print(list(filtered_odd_list))
# Все просто:)
