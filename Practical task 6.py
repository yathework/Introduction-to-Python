# Необходимо написать программу,
# которая будет считывать со стандартного ввода строку,
# далее будет приводить ее к нижнему регистру, а также будет заменять символы “!”, “%”, “#”, “@” на пустую строку.
# В итоге нужно будет вывести в первой строке число замененных символов, а во второй преобразованную строку.
#
# Пример 1
#
# Входные данные
# Hello World!@#%
#
# Выходные данные
# 4
# hello world



# Считываем строку из стандартного ввода
input_string = input().strip()

# Определяем символы, которые нужно удалить
symbols_to_remove = "!%#@"

# Считаем количество символов, которые будут заменены
count_replaced = sum(input_string.count(symbol) for symbol in symbols_to_remove)

# Удаляем указанные символы и приводим строку к нижнему регистру
transformed_string = input_string.lower()
for symbol in symbols_to_remove:
    transformed_string = transformed_string.replace(symbol, "")

# Выводим результат
print(count_replaced)            # Количество замененных символов
print(transformed_string)        # Преобразованная строка