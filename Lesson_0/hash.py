# Чекаем насколько объект хэшебл. Если нет, обрабатываем ошибку и выводим False. Если да, то как бы да

def is_hashable(obj):
	try:
		hash(obj)
		return True
	except TypeError:
		return False

print(is_hashable(str))
print(is_hashable(int))
print(is_hashable(float))
print(is_hashable(list))
print(is_hashable(tuple))
print(is_hashable(set))
print(is_hashable(dict))
print(is_hashable({1: 2}))
print(is_hashable({1,}))
print(is_hashable([2, 4]))
print(is_hashable(('False', True)))