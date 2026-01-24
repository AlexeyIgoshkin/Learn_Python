class Car:
	def move(self):
		print("Car is now moving")

	def stop(self):
		print("Car now stopped")


# Self является ключевым словом, которое означает,
# что функция будет реализована экземпляром класса, а не самим классом


lamborghini = Car()  # создаем экземпляр
bmw = Car()  # еще один

lamborghini.move()  # Вызываем фукнцию класса. Здесь в аргументах зашит self, то есть сам lamborghini.
# то же самое мы можем вызвать вот так:
Car.move(bmw)  # передается на место self явно
# Если передадим так, то получим ошибку:
# lamborghini.move(lamborghini) # Car.move() takes 1 positional argument but 2 were given
# Здесь же мы видим, что один аргумент будто бы передался, но его же нет.
# Потому что при объявлении функции self указывается явно, а при вызове через экземпляр он вшит, запомни это
