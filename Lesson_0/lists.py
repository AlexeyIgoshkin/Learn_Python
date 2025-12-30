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

# ИНВЕРСИЯ ПОСЛЕДОВАТЕЛЬНОСТЕЙ
# Важно! Метод .reverse() инвертирует на месте ТОТ ЖЕ САМЫЙ СПИСОК. Возвращает None.
list_for_reverse_method = [2, True, 4, False, 5, 'Six']
print(list_for_reverse_method)
list_for_reverse_method.reverse()
print(list_for_reverse_method)

# функция reversed() создает новый объект. Очень важно обернуть результат в нужную коллекцию (см. print)
list_for_reversed_function = [2, True, 4, False, 5, 'Six']
print(list_for_reversed_function)
reversed_list_of_function = reversed(list_for_reversed_function)
print(tuple(reversed_list_of_function))

# Способ через слайсер. Хороший способ повыебываться на собесе
list_for_sliced_reverse = [2, True, 4, False, 5, 'Six']
print(list_for_sliced_reverse)
sliced_reversed_list = list_for_sliced_reverse[::-1] # start и stop по умолчанию, а -1 - это обратный порядок
print(sliced_reversed_list)