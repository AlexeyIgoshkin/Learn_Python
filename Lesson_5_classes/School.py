from abc import abstractmethod, ABC


class Group(ABC):  # Является подклассом абстрактного класса, для реализации абстрактных методов
	# Общие характеристики класса для всех объектов
	pupils = True
	school_name = 42
	principal = 'Ivan Petrov'

	# Уникальные характеристики
	def __init__(self, title, pupils_qty, leader):
		self.title = title  # Возьми экземпляр класса и подставь в значение title то, что указано в аргументах экземпляра
		self.pupils_qty = pupils_qty
		self.leader = leader

	def study(self):
		print("Learning")

	@abstractmethod  # Делает метод абстрактным. Все наследники класса ОБЯЗАНЫ его реализовать
	def move(self):
		pass


class PrimaryGroup(Group):
	max_age = 11
	min_age = 6
	building_section = 'left'

	# Можно реализовывать init на основе суперкласса, добавляя параметры:
	def __init__(self, title, pupils_qty, leader, classroom):
		super().__init__(title, pupils_qty, leader)
		self.classroom = classroom

	# Важно. init вызывается иерархически, а значит если в субклассе есть init, то init суперкласса
	# будет проигнорирован. Мы, зная это, вызываем init суперкласса нарочно, а уже потом добавляем свои параметры

	def move(self):
		print("Run fast")


class MediumGroup(Group):
	max_age = 18
	min_age = 14
	building_section = 'right'

	def move(self):
		print('Walks fast')


class HighGroup(Group):
	max_age = 13
	min_age = 12
	building_section = 'center'

	def move(self):
		print("Go slowly")


# Указываем аргументы метода init. При инициализации экземпляра все параметры примут эти уникальные значения аргументов
eleven_grade_a = HighGroup('11a', 24, "Maria Ivanovna")
sixth_grade_c = MediumGroup('6c', 25, 'Veronika Aleksandrovna')
third_grade_b = PrimaryGroup('3b', 29, "Yulia Artemova", 23)

# Можем проверить любой атрибут класса просто распечатав его, например.
print(eleven_grade_a.pupils_qty)
print(sixth_grade_c.leader)
print(third_grade_b.title)
print(third_grade_b.classroom)

eleven_grade_a.move()
sixth_grade_c.move()
third_grade_b.move()
