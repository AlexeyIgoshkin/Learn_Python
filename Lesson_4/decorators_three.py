# Ну а теперь, собственно, DECORATORS. Берем пример из decorators_two
def add_logs(func):  # Параметр декоратора называется func, так принято

	def wrapper():  # Функция обретка, как правило называется wrapper, так тоже принято
		print(f'Function "{func.__name__}" has started')  # __name__ метод, возвращающий имя. Надо знать!
		result = func()
		print(f'Function "{func.__name__}" has ended')
		return result  # Вызывает любую переданную функцию

	return wrapper  # А функция add_logs будет возвращать результат wrapper


# Функция-декоратор говорит с помощью какой функции вызывать функцию ниже, то есть
@add_logs  # = add_logs(simple_one)()
def simple_one():
	print('Very important text')


@add_logs  # = add_logs(simple_two)()
def simple_two():
	print('super important text')


simple_one()  # add_logs(simple_one)()
simple_two()  # add_logs(simple_two)()
