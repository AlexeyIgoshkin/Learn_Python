# del это инструкция, не оператор. Его нельзя сразу кинуть в print, например

new_dict = {"a": 2345, 21: "d2"}

del new_dict['a']
new_dict.__delitem__(21)

print(new_dict)  # пустой словарь, так как оба элемента удалены

new_list = [4, 6, 3]

del new_list[1]
new_list.__delitem__(1)

print(new_list)  # 4
