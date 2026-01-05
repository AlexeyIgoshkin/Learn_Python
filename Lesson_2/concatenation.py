# Не добавляет пробел сам
hello = 'hello'
python = 'python'
string = 'Hello ' + 'Python'
print(string)
print(hello + python)

# Форматирование строк через f-strings
print(f"{hello}, {python}")
print(f"This is text with {hello.capitalize()} and {python.capitalize()}")

new_line = "This is text with {0} and {1}"
new_line = new_line.format(hello, python)
print(new_line)

int1 = 1000
list1 = ['lists']
set1 = {'Sets'}
dict1 = {'dict': 'dict'}
str_python = 'Python'

text = f"I love to write code on {str_python}. I wrote about {int1} lines, worked with {list1} and {set1} and {dict1}"
print(text)
