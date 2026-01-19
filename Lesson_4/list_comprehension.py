# Лист Компрехеншен - так и переводится))) Русского названия нет

# MAP:
origin_list = list(range(1, 30))  # Бахаем список

# new_list = []
# for x in origin_list:
# 	new_list.append(x * 2)

new_list = list(map(lambda x: x * 2, origin_list))  # Можем преобразовать его лямбдой в новый список
print(origin_list)
print(new_list)
# А может сделать еще проще, звучит это примерно так:
new_list = [x * 3 for x in origin_list]  # Умножь элемент на 3 для каждого элемента в списке origin_list
print(new_list)

# FILTER:
origin_list = list(range(1, 30))  # Еще раз бахаем список

new_list = []
for x in origin_list:
	if x % 2 == 0:
		new_list.append(x)
print('Фильтрация for', new_list)

odd_list = []
filtered_lambda_list = filter(lambda x: x % 2 == 0, origin_list)  # Помни, что с лямбдой мы должны конвертировать
filtered_comprehension_if_list = [x for x in origin_list if x % 2 == 0]  # Записывай х для х в списке если х%2=0
filtered_comprehension_if_else_list = \
	[x if x % 2 == 0 else odd_list.append(x) for x in origin_list]  # Можно так, если хотим else

print('Фильтрация лямбда-функцией', tuple(filtered_lambda_list))
print('Фильтрация лист-компрехеншеном', filtered_comprehension_if_list)
print('Фильтрация лист-компрехеншеном с if else', filtered_comprehension_if_else_list)
print('Фильтрация лист-компрехеншеном с if else odd_list', odd_list)

'''
Иерархия как пользоваться этими 3 способами преобразования по части best practices:

for x in origin_list: ДЖУНИОР
new_list = [x * 3 for x in origin_list]: МИДДЛ
new_list = list(map(lambda x: x * 2, origin_list)): СЕНЬОР
'''
