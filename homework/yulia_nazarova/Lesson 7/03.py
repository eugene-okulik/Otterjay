# Программа возвращает результат своей работы в таком виде:
line_one = 'результат операции: 42'
line_two = 'результат операции: 54'
line_three = 'результат работы программы: 209'
line_four = 'результат: 2'


# Получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте
def end_result(line):
    line = line.split()
    print(int(line[-1]) + 10)


end_result(line_one)
end_result(line_two)
end_result(line_three)
end_result(line_four)
