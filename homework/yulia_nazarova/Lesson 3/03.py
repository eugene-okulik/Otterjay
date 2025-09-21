# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

import statistics

num_one = 8
num_two = 2
data = [num_one, num_two]
quantity = len(data) # решила попробовать сделать формулу универсальнее

formula_one = (num_one+num_two)/quantity
print("Среднее арифметическое: " + str(formula_one))

# Нашла такой вариант - через библиотеку statistics
data = [num_one, num_two]
formula_two = statistics.geometric_mean(data)
print("Среднее геометрическое: " + str(formula_two))

