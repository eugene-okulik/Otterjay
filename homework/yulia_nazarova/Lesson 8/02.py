import sys

sys.set_int_max_str_digits(100000)


# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


count = 1
for number in fibonacci(100000):
    if count in {5, 200, 1000, 100000}:
        print(number)
    count += 1
