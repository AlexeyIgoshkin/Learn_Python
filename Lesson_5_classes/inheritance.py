class ExtendedList(list):
	def get_len_info(self):
		print(f'List has {len(self)} elements')


first_list = ExtendedList([4, 5, 612, 6, 26, 34, 634, 6, 88])
second_list = ExtendedList([9999, 32, 5])

first_list.get_len_info()
first_list.append(2)
first_list.get_len_info()
third_list = ExtendedList(first_list + second_list)  # Вот так можем ебануть слияние двух списков, без доп []
third_list.get_len_info()
third_list.sort(reverse=True)  # Отсортируем просто так, потому что можем :)
print(third_list)
