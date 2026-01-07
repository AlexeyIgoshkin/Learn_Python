# Создаем словарь с определенными ключами.
image_dict_true = {"image_id": 5136, "image_title": 'my_cat'}
image_dict_false_id = {"image_name": 5136, "image_title": 'my_cat'}
image_dict_false_title = {"image_id": 5136, "image_name": 'my_cat'}
image_dict_false_all = {"image_age": 5136, "image_name": 'my_cat'}


# Функция с райзом ошибки, если указанных ключей нет в словаре
def image_info(img: dict) -> str:
	if 'image_title' not in img:
		raise TypeError("There is missing image_title key")
	if 'image_id' not in img:
		raise TypeError("There is missing image_id key")
	return f"Image '{img['image_title']}' has id '{img['image_id']}'"


# Вызываем корректный словарь, ошибок не будет
print(image_info(image_dict_true))

# Вызываем остальные словари, где есть ошибка и смотрим как обрабатывает
try:
	print(image_info(image_dict_false_id))
except TypeError as e:  # Поскольку текст TypeError в функции заменен, он и будет отображен
	print(e)

try:
	print(image_info(image_dict_false_title))
except TypeError as e:
	print(e)

try:
	print(image_info(image_dict_false_all))
except TypeError as e:
	print(e.__str__())  # магический метод, эквивалентно print(e)

# А теперь пробуем завернуть все словари в один словарь

dict_of_image_dict = (image_dict_true, image_dict_false_id,
					  image_dict_false_title, image_dict_false_all)  # Класс будет tuple по умолчанию

print(dict_of_image_dict)
# И итеративно по нему пройтись циклом
for el in dict_of_image_dict:
	try:
		print(image_info(el))
	except TypeError as e:
		print(e)
# Получаем тот же результат, что выше в 3 блоках try-except
