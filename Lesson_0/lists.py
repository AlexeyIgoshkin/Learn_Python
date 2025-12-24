# Пустой список можно обявить 2 способами:
first_empty_list = []
second_empty_list = list()
print(first_empty_list, second_empty_list) # [] []


some_list = [1, 2, 'text', True, {4, 5}, [4, 7], ('apple', 'banana'), {'key': 'value'}]
print(some_list)
print(some_list[4])
print(some_list[-1]) # вызов последнего элемента
print(type(some_list[7]))
print(type(some_list[6]))
print(type(some_list[5]))
print(type(some_list[4]))
changed_second_idx = some_list[2] = 'changed_text'
print(changed_second_idx)
print(some_list)
print('До добавления: ', some_list[-1])
some_list.append(False)
print('До добавления: ', some_list[-1])
print(some_list)
some_list.reverse()
print('Реверснутый', some_list)
print(len(some_list))
popped = some_list.pop(-1) # Удаляя элемент из списка, мы можем его сохранить в переменную
print(some_list)
