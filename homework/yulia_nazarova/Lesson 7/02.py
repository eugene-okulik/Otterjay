# Выведите на экран каждый ключ столько раз сколько указано в значении.
# Cделайте так, чтобы каждый ключ печатался в одной строке (как в примере)
# Помните, что копипаст одного и того же кода - плохо

words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
words_list = list(words.items())
# print(words_list[0])
a, b = words_list[0]
c, d = words_list[1]
e, f = words_list[2]
g, h = words_list[3]


def printing_line(key, number):
    print(key * number)


printing_line(a, b)
printing_line(c, d)
printing_line(e, f)
printing_line(g, h)
