import random

# Напишите программу. Есть две переменные, salary и bonus.
# Salary - int, bonus - bool. Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.


salary = int(input('Please enter your salary: '))
bonus = bool(random.randint(0, 1))
if bonus is not True:
    print(f'${salary}')
else:
    print(f'${random.randint(10000, 100000) + salary}')
