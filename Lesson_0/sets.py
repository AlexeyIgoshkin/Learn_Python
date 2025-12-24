# Set - итерируемый Неупорядоченный объект с уникальными значениями.
# Изменяемый, но индекса нет, так как нет порядка.


some_set = {False, 2, 'Third', 2, 34, True, (2, 2)}
some_list1 = list(some_set)
some_list2 = list(reversed(some_list1))  # Развернуть set, и обязательно преобразовать в список для вывода
print(some_list1)
print(some_list2)

union_dict = dict(zip(some_list1, some_list2))  # Можно преобразовать в словарь 2 списка, также явно приводим тип
print(union_dict)

print(some_set)
some_set.add(3)
some_set.add(34)
print(some_set)

new_empty_dict = {} # так создается только пустой словарь
new_empty_set = set() # пустой set можно создать только так
new_empty_dict2 = dict() # пустой set можно создать только так

print(type(new_empty_dict), type(new_empty_set), new_empty_dict2)
