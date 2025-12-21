meal_dict = {
	'Картошка': 70,
	'Редиска': 20,
	'Апельсиновый сок': 60,
	'Банан': 50,
	'Хлеб': {
		'Цельнозерновой': "40-55",
		'Ржаной': 30-50,
		'Отрубной': 50-60,
		'Белый': 75-85,
	}
}

meal_tpl = (
	('Картошка', 'картошки', 70),
	('Редиска', 'Редиски', 20),
	('Апельсиновый сок', 'Апельсинового сока', 70),
)

def get_glycemic_idx(meal_name):
	if meal_name in meal_dict:
		value = meal_dict[meal_name]
		if isinstance(value, dict):
			print(f'Гликемический индекс {meal_name.lower()}:')
			for sub_key, sub_value in value.items():
				print(f"  {sub_key}: {sub_value}")
		else:

			print(f'Гликемический индекс {meal_name.lower()}: {value}')

	else:
		print(f"Продукта '{meal_name}' нет в списке")
	return


def get_recommendation(idx_value: int):
	if idx_value <= 50:
		return "Хороший выбор"
	elif idx_value <=69:
		return "Следует ограничить"
	else:
		return "Воздержитесь от употребления"

typed_meal_name = input("Введите название продукта: ").capitalize()

get_glycemic_idx(typed_meal_name)