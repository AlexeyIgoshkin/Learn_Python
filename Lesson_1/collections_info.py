# Инфа о любой коллекции в разных функциях.
# Пишем функции:


def get_collection_class_name(obj):
	message = "Object type is {0}."
	return print(message.format(type(obj)))


def get_collection_elements(obj):
	try:
		if isinstance(obj, str):
			print(f"Collection elements: '{obj}'")
			return
		if isinstance(obj, dict):
			dict_items = [f"{key} = {value}" for key, value in obj.items()]
			print(f"Collection elements: '{dict_items}'")
			return
		else:
			collection_to_string = ', '.join(map(str, obj))
			print("Collection elements:", collection_to_string)
	except TypeError:
		print("Not collection type. No elements to display")


def get_collection_length(obj):
	try:
		print("Elements quantity:", len(obj))
	except TypeError:
		print("Elements quantity: None. This type has no length.")
	return


def is_hashable(obj):
	try:
		obj_hash = hash(obj)
		print(f"Hash of this object: {obj_hash}")
		return True
	except TypeError:
		print(f"{type(obj)} is not hashable.")
		return False


def has_unique_elements(obj):
	temp_list = []
	try:
		for x in obj:
			if x in temp_list:
				print(f"Collection has not-unique elements ({x}, for example)")
				return False
			temp_list.append(x)
		print(f"Collection has only unique elements")
		return True
	except TypeError:
		print(f"Collection is not iterable, so no seeking unique elements")
		return False


def is_ordered(collection):
	if isinstance(collection, (list, tuple, str, dict)):
		print("Collection has ordered insertion.")
		return True
	if isinstance(collection, (set, frozenset)):
		print("Collection has no order.")
		return False
	print(type(collection), "is not a collection type, so no ordering in its elements.")
	return False


def is_mutable(collection):
		if isinstance(collection, (list, dict, set)):
			print("Collection is mutable.")
			return True
		if isinstance(collection, (tuple, str, frozenset)):
			print("Collection is not mutable.")
			return False
		print(f"Object is not a collection, so no need to check if it is mutable" )
		return False


def separator():
	print('-' * 50)

# Создаем коллбэк функцию
def check_collection_info(collection):
	get_collection_class_name(collection)
	get_collection_elements(collection)
	get_collection_length(collection)
	is_hashable(collection)
	is_mutable(collection)
	is_ordered(collection)
	has_unique_elements(collection)
	separator()


# Создаем разные итерации:
my_list = [1, 2, 'double', True, True, 6, 2, 3, 2]
my_tuple = (0, False, {'dict_key': 'dict_value'}, 4, ['False', True], 6, -32)
my_set = {1, 2, 3, 4, 5, 6, 6, 6}
my_dict = {1: 'one', 2: 'two', 3: True, 4: False, 5: 'What the FUCK!?', 6: 3.14}
my_string = "There is no impossible!"
my_frozenset = {1, 3, 5, 6, 7}
my_int = 22225
my_float = 3.14

# Сейчас будет ебанутый подход. Мне так захотелось.
# Запихиваем в переменную все коллекции
examples = my_list, my_tuple, my_set, my_dict, my_string, my_frozenset, my_int, my_float

# И вызываем коллбэк через цикл. На нахуй!
for i in examples:
	check_collection_info(i)
