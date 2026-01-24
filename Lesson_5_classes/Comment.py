class Comment:
	# Init определяет собственные атрибуты экземпляров классов. Ее не нужно вызывать.
	# Она автоматом реализуется при создании экземпляра класса
	def __init__(self, text):  # Функция-конструктор, вызывается сразу с созданием экземпляра
		self.text = text  # Указывает, что text от экземпляра класса будет равен аргументу text в функции init
		self.votes_qty = 0  # Указывает, что votes_qty конкретного класса будет равен 0 после инициализации

	def upvote(self):
		self.votes_qty += 1  # А затем мы уже можем изменять votes_qty другими функциями экземпляра


first_comment = Comment("My first comment")  # Экземпляр создается и передается в функцию init класса Comment
# Передается в качестве значения для первого параметра, self
# Далее для созданного объекта self добавляется собственных 2 аттрибута: text и votes_qty, присваивает значения
second_comment = Comment("My second comment")

first_comment.upvote()  # Теперь вызвав несколько раз upvote, мы можем проследить что...
first_comment.upvote()
first_comment.upvote()
first_comment.upvote()
first_comment.upvote()
print(first_comment.votes_qty)  # ...значение собственного атрибута votes_qty для first_comment меняется
print(second_comment.votes_qty)  # А значение собственного атрибута votes_qty для другого экземпляра не меняется
print(first_comment.text)
first_comment.text = "Changed attribute"  # Дальше можно менять атрибуты как угодно
print(first_comment.text)

print(first_comment.__dict__)  # Можно посмотреть какие атрибуты и значения есть у экземпляра
print(first_comment)  # <__main__.Comment object at 0x000001F54D4A0C20>
# __main__. означает, что выполнение происходит напрямую с помощью интерпритора

second_comment.upvote = 10  # Что мы тут сделали? Это очень интересно.
# На самом деле мы не переписали значение для функции upvote на уровне класса,
# мы добавили уникальный атрибут upvote в экземпляр класса second_comment.

print(first_comment.votes_qty)  # 5. Значит все верно, НО
# теперь second_comment.upvote() НЕ СРАБОТАЕТ, потому что Питон найдет upvote в атрибутах
# и не пойдет дальше, на уровень функций класса, в результате ошибка int not callable нам в морду
