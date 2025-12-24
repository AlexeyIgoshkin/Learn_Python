# Неизменяемый тип итерируемого объекта
some_tuple = (4, 5, 'text', False, [231, 4221], 5)
third_tuple_idx = some_tuple[3] # к кортежу можно обращаться по индексу
print(third_tuple_idx)
print(some_tuple.count(5)) # сколько раз встречается значение
print(list(some_tuple))

single_tuple = (2,) # Котрежи с одним элементом будут восприниматься как int, поэтому нужно ставить запятую
print(single_tuple)
print(type(single_tuple))
