try:
	user_input = int(input('Введите число: '))
	# Правильное условие (отсечение неиспользованных условий)
	if user_input == 1:
		print("Число равно 1")
	elif user_input == 2:
		print("Число равно 2")
	else:
		print("Какое-то число")

	# Не очень правильно (каждое условие проверится в любом случае)
	if user_input == 1:
		print("Число равно 1")
	if user_input == 2:
		print("Число равно 2")
	if user_input not in (1, 2):
		print("Какое-то число")
except ValueError:
	print("Ты ввел строку")

