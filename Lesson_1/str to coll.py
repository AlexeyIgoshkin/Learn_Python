# Преобразовать из строки и итербл

new_string = 'Banana Apple Orange Strawberry'
list_from_string = new_string.split() # если ничего не укажем, каждое слово = отдельный элемент списка
list_from_string_with_arg = new_string.split(',') # если укажем - закинет весь текст в один элемент
print(list_from_string)
print(list_from_string_with_arg)

new_string2 = 'Banana, Apple, Orange, Strawberry'
list_from_string2 = new_string2.split(',') # если указываем элемент, который есть в строке - разделите по этому символу
print(list_from_string2)

# Преобразование из итербл в строку
new_set = {'Banana', 'Apple', 'Orange', 'Strawberry'} # для разообразия использую сет
# ниже крутая штука - соединяет множество элементов по шаблону в строке
# синтаксис необычный, надо запомнить - сначала то, что будет между элементами, затем .join(коллекция)
string_from_set = ', '.join(new_set)
print(string_from_set)

# пример в отрыве, если собираем данные откуда-то
# к слову о подстановках в строках :)

username = 'Василий'

print('Клиент', username, 'очень любит следующие продукты:', string_from_set) #1 ставит пробелы, но неудобно
print('Клиент ' + username + ' очень любит следующие продукты: ' + string_from_set) #2 не ставит пробелы, неудобно
print(f'Клиент {username} очень любит следующие продукты: {string_from_set}') #3 предпочтительный варик, удобно
my_text = 'Клиент %s очень любит следующие продукты: %s' #4 тоже такой себе вариант, но есть
print(my_text % (username, string_from_set)) # % передаем позиционно что печатать в строке, передается в кортеже
my_text = 'Клиент {1} очень любит следующие продукты: {0}' #5 тот же метод подстановки, что 3, но через метод format
print(my_text.format(username, string_from_set)) # плейсхолдеры надо нумеровать. Смотри в распечатке какая х-ня))


# Данные подстановки должны быть подготовлены ДО того, как переменная будет подставлена, иначе fail:
message = 'Привет, {0}'
# print(f'Привет, {read_name}') # Здесь все наебнется, потому что read_name появится только на след строке
read_name = input('Введи свое имя: ')
print(f'Привет, {read_name}') # А здесь все будет хорошо, так как read_name инициализирована
print(message.format(read_name)) # ну и здесь тоже нормально
