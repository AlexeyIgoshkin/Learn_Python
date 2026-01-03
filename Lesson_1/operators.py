# Арифметические операторы: +, -, /, *
# Сравнительные операторы: ==, !=, <, >
# Логические операторы: not, and, or
# Текстовые операторы: not, and, or, is, is not, in, not in
# Оператор присвоения: =
# Унарные операторы: -my_number, +my_number (конвертация в число), not (not not)is_activated
# Бинарные операторы (инфиксная запись): =, +, +=, ==, and

# for x in range(1, 101):
# 	print(x, id(x), (hex(id(x))))

first_set = {2, 5, True, 'seven', 25.4, False}
second_set = {2, True, 'seven', 25.4, False, 5}
print(first_set is second_set) # Сравниваются ОБЪЕКТЫ (ID)
print(first_set == second_set) # Сравниваются ТОЛЬКО ЗНАЧЕНИЯ
print(first_set.__eq__(second_set)) # Эквивалентно предыдущей записи
print('2' in second_set)
print('2' not in second_set)
print(2 in first_set)
try:
	print([] in first_set) # НЕЛЬЗЯ добавлять ИЗМЕНЯЕМЫЙ объект в SET

except TypeError:
	print('НЕЛЬЗЯ добавлять ИЗМЕНЯЕМЫЙ объект в SET')
