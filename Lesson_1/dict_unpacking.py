# Распаковка и замена ключей

main_button = {
	'width': 400,
	'height': 200,
	'text': 'Confirm',
	'color': 'white'
}

orange_button = {
	**main_button,  # Порядок важен, так как в обратном порядке цвет будет заменен изначальным
	'color': 'orange'
}

print(main_button)
print(orange_button)

# Объединяем через черту |. Порядок важен, если есть одинаковые ключи

size_button = {
	'width': 400,
	'height': 200
}
text_button = {
	'text': 'Confirm',
	'color': 'white'
}

color_button = {
	'color': 'black'
}

united_button = size_button | text_button | color_button
print(united_button)
