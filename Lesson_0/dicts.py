# dict = словарь, упорядоченный итерируемый объект "ключ-значение", изменяемый, порядок сохраняется
# ключ должен быть объектом неизменяемого типы

some_dict = {1: 'First', 2: 'Second', 3: 'Third', 4: 'Fourth', False: True, 'True': False, (2,): (3,)}
print(some_dict[3]) # Обращение по ключу
print(some_dict[False])
print(some_dict["True"])
print(some_dict[2,])
print(len(some_dict)) # узнаем длину
some_dict[3] = 'New Value' # меняем значение
print(some_dict[3])

some_dict['New key'] = True # добавляем значение (если его нет, Питон добавит)
print(some_dict)
print(len(some_dict))

some_list_of_some_dict = list(some_dict)
print(some_list_of_some_dict)

print(some_dict.keys()) # выборка всех ключей
print(some_dict.values()) # выборка всех значений
print(some_dict.items()) # выборка всех элементов
