words_1 = input('Введите проверяемые слова через пробел: ').split()
root_1 = input('Введите первый корень: ')
words_2 = input('Введите проверяемые слова через пробел: ').split()
root_2 = input('Введите второй корень: ')
root_words_1 = []
root_words_2 = []

def single_root_words():
    for word in words_1:
        is_word_1 = root_1.lower() in word.lower()
        if is_word_1 == True:
            root_words_1.append(word)
    for word in words_2:
        is_word_2 = root_2.lower() in word.lower()
        if is_word_2 == True:
            root_words_2.append(word)
    print(*root_words_1)
    print(*root_words_2)

single_root_words()