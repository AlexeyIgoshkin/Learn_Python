fruits = ('banana', 'apple', 'strawberry')  # можно и со списком, и с кортежем и так далее

banana, apple, strawberry = fruits  # присваивание каждому элементу списка собственной переменной
print(type(fruits))  # узнаем тип объекта
print(fruits)
print(', '.join(fruits))  # печатаем с разбиением в str

vegetables = ['potato', 'tomato', 'cucumber']

potato, *remaining_vegetables = vegetables  # *означает что оставшиеся элементы мы кладем в одну переменную

print(potato)  # класс с одним элементом будет str
print(type(potato))  # так и есть
print(remaining_vegetables)  # возвращает ту же коллекцию

# Можно распаковывать например словарь прямо в аргументы функции
user_profile = {
	'name': 'Alexey',
	'comments_qty': 35
}  # подготовили словарь

user_profile_list = ['Alexey', 35]


def user_info(name, comments_qty=0):  # мы обязаны дать name в словаре, qty можно не давать, по умолчанию 0
	if not comments_qty:  # если qty = 0
		return f'{name} has no comments'  # возвращаем что у юзера нет комментов
	return f'{name} has {comments_qty} comments'  # иначе передаем кол-во комментов из словаря


# в качестве аргументов передаем словарь выше
print(user_info(**user_profile))  # Вызов через **, если словарь на подойдет по аргументам, вернется TypeError
print(user_info(user_profile['name'], user_profile['comments_qty']))  # позиционные аргументы
print(user_info(name=user_profile['name'], comments_qty=user_profile['comments_qty']))  # именованые аргументы

print(user_info(*user_profile_list))  # Вызовом через * распаковываем список в позиционные аргументы
print(user_info(user_profile_list[0], user_profile_list[1]))  # Через индекс тоже можем
print(user_info(name=user_profile_list[0], comments_qty=user_profile_list[1]))  # И через имена параметров

my_name, my_comments_qty = user_profile_list  # а можем распаковать список отдельно
print(user_info(my_name, my_comments_qty))  # и передать в функцию уже переменные

# Задание
list_of_dicts = [
	{'age': 20, 'nickname': 'Nagibator666'},
	{'age': 30, 'nickname': 'BacRH'},
	{'age': 40, 'nickname': '120ый'}
]

first, second, third = list_of_dicts  # распаковываем список словарей по переменным


def player_info(age, nickname=''):
	if not nickname:
		return f'Возвраст игрока без никнейма: {age}'
	return f'Игроку {nickname} {age} годиков'


print(player_info(**first))
print(player_info(**second))
print(player_info(**third))
print(player_info(nickname=first['nickname'], age=third['nickname']))  # можем ставить значения разных словарей :)
print(player_info(age=second['nickname']))
