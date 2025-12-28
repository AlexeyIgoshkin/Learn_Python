# Распаковка списка. Можем сделать так, если точно знаем сколько элементов в коллекции

# СПИСКИ, КОРТЕЖИ
first_list  = [1, 3, 5, 9]
one, two, three, four = first_list
print(one, two, three, four, sep='')


# Слайсер. Можно проводить выборку из коллекции с любыми условиями и даже развернуть ее
second_tuple = (4, True, 'Soccer', 13.2, [4, False], 156)
sliced_tuple = second_tuple[2:6:2] # Начиная:до(не включительно):шаг
sliced_tuple2 = second_tuple[6:2:-1] # Отрицательный шаг означает движение с конца
print(sliced_tuple)
print(sliced_tuple2)

# Способы развенуть строку. Reversed и Slicer. Не являются even (только если преобразовать в tuple)
print('Являются ли объекты even при reversed:', reversed(second_tuple) == second_tuple[::-1])
print('Являются ли объекты even при преобразовании в кортеж:',
	  tuple(reversed(second_tuple)) == second_tuple[::-1])
print('Id reversed:', id(reversed(second_tuple)))
print('Id sliced:', id(second_tuple[::-1]))
print('Type reversed:', type(reversed(second_tuple)))
print('Type sliced:', type(second_tuple[::-1]))
