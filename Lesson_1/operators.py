# Арифметические операторы: +, -, /, *
# Сравнительные операторы: ==, !=, <, >
# Логические операторы: not, and, or
# Текстовые операторы: not, and, or, is, is not, in, not in
# Оператор присвоения: =
# Унарные операторы: -my_number, +my_number (конвертация в число), not (not not)is_activated
# Бинарные операторы (инфиксная запись): =, +, +=, ==, and
from Lesson_1.collections_info import my_dict

# for x in range(1, 101):
# 	print(x, id(x), (hex(id(x))))

first_set = {2, 5, True, 'seven', 25.4, False}
second_set = {2, True, 'seven', 25.4, False, 5}
print(first_set is second_set)  # Сравниваются ОБЪЕКТЫ (ID)
print(first_set == second_set)  # Сравниваются ТОЛЬКО ЗНАЧЕНИЯ
print(first_set.__eq__(second_set))  # Эквивалентно предыдущей записи
print('2' in second_set)
print('2' not in second_set)
print(2 in first_set)
try:
	print([] in first_set)  # НЕЛЬЗЯ добавлять ИЗМЕНЯЕМЫЙ объект в SET
except TypeError:
	print('НЕЛЬЗЯ добавлять ИЗМЕНЯЕМЫЙ объект в SET')

# or и and - операторы короткого замыкания. Это значит что в выражении
# x = x and y = y Питон вычислит сначала 1-ое выражение. Если оно ложно, он не станет отрабатывать дальше и вернет его
# Если же выражение правдиво, то он проверит 2-ое выражение и вернет его значение, каким бы оно не было
# or - работает по-другому: если выражение 1 истинно, то нет смысла рассматривать 2-ой операнд
# Если выражение 1 ложно, Питон продолжит оценку выражений. 2 выражение будет результатом всего выражения.

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
print(my_list1 or my_list2)  # Только первое выражение, потому что оно True
print(my_list1 and my_list2)  # Только второе выражение, потому что все выражение True
my_list3 = []
print(not not my_list3)  # Добиться True False можно через унарник not и двойное отрицание not not

my_dict1 = {}
print(bool(my_dict1 or my_list2))
print(bool(my_dict1 and my_list2))

my_dict2 = {2: 4, 23: 5, True: 'Dictionary'}
my_dict3 = {True: 'Dictionary', 23: 5, 2: 4}
print("Dictionaries are equal" if my_dict2 == my_dict3 else "Dictionaries are not equal")  # Сравнение значений
print("Dictionaries are equal" if my_dict2 is my_dict3 else "Dictionaries are not equal")  # Сравнение по ID
print("Dictionaries are equal" if my_dict2 and my_dict3 else "Dictionaries are not equal")  # Если оба True
print("Dictionaries are equal" if my_dict2 or my_dict3 else "Dictionaries are not equal")  # Если один из них True
