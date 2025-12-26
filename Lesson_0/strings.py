# str - класс строки в Питоне, неизменямый тип, итерируемый объект

list_from_string = list('String')
tuple_from_string = tuple('String')
set_from_string = set('String')
print(list_from_string)
print(tuple_from_string)
print(set_from_string)

union_from_strings = zip(tuple_from_string, set_from_string) # объедияем колекции строк
print(dict(union_from_strings))

print('-' * 30) # можно множить строку вот так
