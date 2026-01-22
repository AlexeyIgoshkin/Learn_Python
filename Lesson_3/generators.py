from sys import getsizeof

# Генератор - последовательность, которая занимает значительно меньше памяти, чем итерация листа, например

nums = (2, 4, 5)
squares_nums_gen = (num * num for num in nums)

print(squares_nums_gen)
print(type(squares_nums_gen))
print(getsizeof(squares_nums_gen))

squares_range_gen = (num * num for num in range(1_000_000))
squares_list_gen = [num * num for num in range(1_000_000)]

print(squares_range_gen)
print(type(squares_range_gen))
print(getsizeof(squares_range_gen))  # В байтах
print(getsizeof(squares_list_gen))  # В байтах
