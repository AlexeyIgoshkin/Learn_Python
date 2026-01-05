# Лямбда функции всегда анонимны. По pep-8 не стоит присваивать лямбда-функции переменные

l1 = lambda a, b: a * b
print(l1) # <function <lambda> at 0x0000013A3BC33530>

# def greeting(greet):
# 	def info(name):
# 		return f"{greet}, {name}!"
# 	return info
# То же самое, но с лямбдой:

def greeting(greet):
	return lambda name: f"{greet}, {name}!"

morning_greeting = greeting("Good morning")
print(morning_greeting) # <function greeting.<locals>.<lambda> at 0x0000019844720930>
print(morning_greeting('Alexey')) # Good morning, Alexey!