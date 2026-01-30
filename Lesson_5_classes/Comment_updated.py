class Comment:
	def __init__(self, text, initial_votes_qty=0):  # значение по умолчанию 0
		self.text = text
		self.votes_qty = initial_votes_qty

	def __add__(self, other):  # Можно создавать свои магические методы, их реализацию
		return f'{self.text}, {other.text}', self.votes_qty + other.votes_qty

	# по умолчанию кортеж, но можно любой итерируемый тип, даже словарь по типу
	# return {
	#     text: f'{self.text}, {other.text}'
	#	  votes_qty: self.votes_qty + other.votes_qty
	# }

	def upvote(self, qty=1):
		self.votes_qty += qty

	def reset_votes_qty(self):
		self.votes_qty = 0


first_comment = Comment("First comment")  # votes_qty 0
second_comment = Comment("First comment", 4)  # votes_qty 4

first_comment.upvote()  # votes_qty += 1
second_comment.upvote(5)  # votes_qty += 5

print(first_comment.votes_qty)  # 1
print(second_comment.votes_qty)  # 9

first_comment.reset_votes_qty()  # votes_qty = 0
second_comment.reset_votes_qty()  # votes_qty = 0

print(first_comment.votes_qty)  # 0
print(second_comment.votes_qty)  # 0

print(first_comment + second_comment)  # Использование нашего __add__ для экземплятор Comment. Переопредили стандартный
