# Ложными значениями считаются все пустые последовательности, любой 0, и False

print("Функция bool для значений:")
print('0:', bool(0))
print('0.1:', bool(0.1))
print('0j:', bool(0j))
print('bool:', bool(bool))
print('None:', bool(None))
print('[]:', bool([]))
print('{}:', bool({}))
print('():', bool(()))
print('set():', bool(set()))
print('str empty:', bool(''))
print('str not empty:', bool('str'))
print('range:', bool(range(0)))
print('Not []:', not [])
print('Not not[]:', not not[])

# Условная инструкция. Оба кода идентичные:
my_list = [1, 2, 3]
if len(my_list) > 0:
	print("My list has elements (len)")
if my_list: # Писать надо вот так, поскольку так быстрее и короче, а суть та же
	print("My list has elements (if my_list)")
