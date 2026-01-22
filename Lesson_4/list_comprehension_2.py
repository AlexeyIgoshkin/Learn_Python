original_num_list = [-2, 3, 14, -45, 4, -199, 2]

# 3 способа преобразовать список на примере абсолютных значений с условием:

absolute_nums_for_in = []
for num in original_num_list:
	absolute_nums_for_in.append(abs(num))

absolute_nums_comprehension = [abs(num) if num > 0 else 0 for num in original_num_list]

absolute_nums_map_lambda = list(map(abs, filter(lambda x: x > 0, original_num_list)))

print(original_num_list)

print(absolute_nums_for_in)
print(absolute_nums_comprehension)
print(absolute_nums_map_lambda)
