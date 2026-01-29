# Самостоятельная работа:


class Image:
	total_images = 0

	def __init__(self, resolution, title, extension):
		self.resolution = resolution
		self.title = title
		self.extension = extension
		Image.total_images += 1

	def resize(self, value: str):
		self.resolution = value

	def set_extension(self, extension):
		self.extension = extension

	def title_capitalize(self, cap: str):
		self.title = cap.capitalize()

	def __str__(self):  # Важно! Конвертация объекта в строку через магический метод
		return self.title + self.extension  # print(экземпляр)

	@staticmethod  # Статика. Метод не привязан к экземпляру. Может вызываться на уровне класса
	def merge_comments(first, second):
		return f"{first}, {second}"


image_one = Image('1920x1080', 'foreground', '.jpg')
image_two = Image('1280x720', 'background', '.png')
image_three = Image('640x480', 'dog', '.webp')

print(image_one.resolution)
image_one.resize('1024x768')
print(image_one.resolution)
print(image_two.resolution)
image_two.resize('2560x1440')
print(image_two.resolution)
print(image_three.extension)
image_three.set_extension('.gif')
print(image_three.extension)

print(image_two.title)
image_two.title_capitalize('center')
print(image_two.title)

print(image_one)
print(image_two)
print(image_three)

print(isinstance(image_two, Image))  # Принадлежность к классу
print(type(image_three) == Image)

m1 = Image.merge_comments('Suck', 'dick')
print(m1)

print(Image.total_images)
