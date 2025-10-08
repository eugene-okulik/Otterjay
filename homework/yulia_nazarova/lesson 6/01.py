# Добавить ing в конце каждого слова, учитывая знаки препинания

text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, ' \
       'dignissim vitae libero'

words = text.split()
for word in words:
    if word.endswith(','):
        word = word.replace(',', 'ing')
        print(word, end=', ')
    elif word.endswith('.'):
        word = word.replace('.', 'ing')
        print(word, end='. ')
    else:
        print(word + 'ing', end=' ')
