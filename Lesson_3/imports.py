import random
import sys

print(sys.platform)
import os

print(os.path)
from Lesson_2.lambda_func import greeting as go # Импортируем отдельную функцию из файла. С алиасом. Можно и без

print(go('Zdarova')('Chel'))  # и можем использовать со своими данными

rnd1 = random.randint(1, 100)  # Оба числа включительно
rnd2 = random.randint(1, 100)  # Оба числа включительно
rnd3 = random.randrange(1, 100)  # START - включительно, STOP - НЕ включительно


def get_amount(a, b):
	print(f'First number: {a}\n'
		  f'Second number: {b}')
	return a * b


print(get_amount(rnd1, rnd2))  # рандомно перемножает числа
print(random.random() * get_amount(rnd1, rnd2))  # принимает значение в пределах 0.1
# и умножает на результат функции get_amount


users_list = ['Petya', 'Vasya', 'Valera', 'Nickolai', 'Alexey', 'Roman']
print(random.choice(users_list))  # Выбирает случайный объект списка
print(users_list[random.randrange(0, len(users_list))])  # Делает то же самое, но не так красиво
