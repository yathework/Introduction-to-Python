# Необходимо написать программу,
# которая будет считывать со стандартного ввода
# название города и время и выводить информацию
# в формате “Current location is [Location] and time is [Time]”.


# Считываем данные со стандартного ввода
city = input().strip()
time = input().strip()

# Формируем и выводим результат
print(f"Current location is {city} and time is {time}")