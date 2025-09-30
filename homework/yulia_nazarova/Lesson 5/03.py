# Даны такие списки:
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

# Var 1
s_1, s_2, s_3 = students
sub_1, sub_2, sub_3 = subjects
my_text = f'Students {s_1}, {s_2}, {s_3} study these subjects: {sub_1}, {sub_2}, {sub_3}'
print(my_text)

# Var 2
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
