# создать функцию с двумя листами, объединить в словарь, вернуть его из функции и распечатать

def merge_lists_do_dict(list_one: list, list_two: list):
	#united_lists = dict(zip(list_one, list_two))
	#return united_lists
	return dict(zip(list_one, list_two)) # а можно вот так ебануть


dictionary_one = merge_lists_do_dict([1, 2, 3], ['one', 'two', 'three'])
dictionary_two = merge_lists_do_dict([(), 'True', False], [(1,3,5), {2, 4}, {1: 45}])

print(dictionary_one)
print(dictionary_two)
