from ftplib import print_line

my_list = [True, 3, 'Network', 23.4, False, [32, 23]]

# Не надо так делать
names_list = ['James', 'Tom', 'Jim', 'Bill', 'Chris', 'Jonathan']
James, Tom, Jim, Bill, Chris, Jonathan = names_list # Распаковка списка
#print(Chris)

names_to_string = ', '.join(names_list)
#print(names_to_string)

# для каждого элемента из этой коллекции
empty_list = []
for name in names_list:
	if name == James:
		print(name)
	else:
		empty_list.append(name)
print(', '.join(empty_list))

# Распечатываем мужиков через Mr, чье имя начинается на J, меняем i на I
for name in names_list:
	name = name.replace('i', 'I')
	if name.startswith('J'):
		print("Mr. ", end="")
	print(name)

# Словарь и циклы. Можем печатать ключи, значения и все вместе:
names_dict = {'James': 23, 'Tom': 16, 'Jim': 23, 'Bill': 44, 'Chris': 32, 'Jonathan': 49}
for name in names_dict:
	print(name + ': ' + str(names_dict[name]))
print(names_dict.items())

# Обращаемся к items, распакуем имя и возраст по переменным из кортежа person:
for name, age in names_dict.items():
	# name, age = person
	print(f"Имя: {name}, возраст: {age}")

text = "Распечатать все слова в которых находится буква О, остальные отбросить и распечатать отдельно"
text_list = text.split()
new_list = []
for word in text_list:
	if 'о' not in word.lower():
		new_list.append(word)
	else:
		print(word)
print(' '.join(new_list))
