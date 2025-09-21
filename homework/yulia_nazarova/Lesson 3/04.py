# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
import math

c_one = 6
c_two = 8

hypotenuse_sq = c_one**2 + c_two**2
hypotenuse = math.sqrt(hypotenuse_sq) # как корень находить поняла только через библиотеку math
print("Гипотенуза равна: " + str(hypotenuse))

# Формула Герона S = √(p(p-a)(p-b)(p-c))
p = (c_one + c_two+hypotenuse) / 2
area = math.sqrt(p * (p - c_one) * (p - c_two) * (p - hypotenuse))
print("Площадь равна: " + str(area))
