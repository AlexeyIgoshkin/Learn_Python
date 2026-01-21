import random


# Бесконечный цикл: while True - мы можем управлять им через break и continue
def first_while_cycle():
	while True:
		random_num = random.randint(1, 5)
		guess_num = int(input('Guess the number from 1 to 5: '))
		if guess_num != random_num:
			print(f'Wrong. Correct number was {random_num}')
			continue  # Означает, что блок кода вернется на исходную для следующей итерации
		print(f'Correct. Good guess. It is {guess_num}. You are brilliant!')
		break  # Означает выход из цикла


def homework_while_cycle():
	while True:
		try:
			first_number = float(input('Type first number: '))
			second_number = float(input('Type second number: '))
		except ValueError as e:
			print(e, 'Type correct numbers')
			continue
		if second_number == 0:
			print('Number must be not 0')
			continue
		print(first_number / second_number)
		proceed_question = input('Do you want to continue? (yes/no): ')
		if proceed_question == 'no':
			break


homework_while_cycle()
