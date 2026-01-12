import datetime

now = datetime.datetime.now()
print("Now:", now)
print("Day of week by index:", now.weekday())
print("Day of week by iso:", now.isoweekday())
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Time from linux origin:", now.timestamp())
print("Tuple representation:", now.timetuple())
print("Time with timezone:", now.timetz())
print("Time:", now.time())

easy_date = datetime.datetime(1960, 11, 2, 22, 21, 53)  # указываем прямо
print(easy_date)

some_time = "2025/11/25 12 hours 12 minutes 56 seconds"
# Можем создать шаблон для парсинга через специальные %.
# Найти их можно на https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
python_date = datetime.datetime.strptime(some_time, '%Y/%m/%d %H hours %M minutes %S seconds')
print(python_date)
print(python_date.time())
print(python_date.date())
human_date = python_date.strftime('Year: %Y-%m-%d, Time: %H:%M:%S')  # А теперь можем указать в каком формате хотим мы
print(human_date)
