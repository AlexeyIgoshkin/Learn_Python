# dict = словарь, упорядоченный итерируемый объект "ключ-значение", изменяемый, порядок сохраняется
# ключ должен быть объектом неизменяемого типы
from copy import deepcopy

some_dict = {1: 'First',
			 2: 'Second',
			 3: 'Third',
			 4: 'Fourth',
			 'list': [1, 2, 3],
			 False: True,
			 'True': False,
			 (2,): (3,)}
# если в копию вложен изменяемый объект, то его ссылка сохранится, и при изменении этих значений,
# изменяться будут и значения копии, и значения оригинала. Чтобы избежать, нужно использовать deepcopy из copy модуля

some_dict_shallow_copy = some_dict.copy() # создали шаллоу копию, где ссылка на список копируется
some_dict_deepcopy = deepcopy(some_dict) # создали глубокую копию, ссылка на список не копируется
some_dict['list'].append(4) # добавляем в ключ list новый элемент списка 4
some_dict_deepcopy['list'].append(True)
print(some_dict)
print(some_dict_shallow_copy)
print(some_dict_deepcopy)

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
