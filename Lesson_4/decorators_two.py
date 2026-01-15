# Продолжаем разбор функций. Как мы бы делали без декоратора:
def add_text(func):

	def wrapper():  # Функция обретка
		print('before')
		func()  # Вызывает любую переданную функцию
		print('after')

	return wrapper  # А функция add_text будет возвращать результат wrapper


def simple_one():
	print('Very important text')


simple_one()
simple_one = add_text(simple_one)  # Результат работы функции add_text с переданной в нее переменной,
# хранящей функцию simple_one
simple_one()  # Теперь мы можем не вызывать add_text(simple_one)


def simple_two():
	print('super important text')


simple_two()
simple_two = add_text(simple_two)
simple_two()
