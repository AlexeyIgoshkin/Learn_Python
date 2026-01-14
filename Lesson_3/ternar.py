# Почему тернарный оператор? Потому что у него 3 операнда

number = 23
print("It is int") if type(number) is int else print("It is not int")

product_qty = list(range(-20, 20))  # Выкупай как можно быстро заполнить итератора цифрами

for x in product_qty:
	print("In stock") if product_qty[x] > 0 else print("Out in stock")

temperature = +23
temp = 'Hot' if temperature > 0 else 'Cold'  # Можно заворачивать в переменную
print(temp)

my_img = ('1920', '1080')
resolution = f"{my_img[0]}x{my_img[1]}" if (len(my_img) == 2 and
											type(my_img[0]) is str and
											type(my_img[1]) is str) else 'incorrect image format'
print(resolution)

# Чекаем длину строки по pep-8
string = 'I love cookies and cache for they simplicity and usefulness in protection of user information'

string_length_checking = 'String is too long' if len(string) > 79 else 'String is valid to pep-8'
print(string_length_checking)
