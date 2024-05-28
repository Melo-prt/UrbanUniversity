words = input('Введите проверяемые слова через пробел: ').split()
root = input('Введите корень слова: ')
root_words = []

def single_root_words():
    for word in words:
        is_word = root.lower() in word.lower()
        if is_word == True:
            root_words.append(word)
    print('Однокоренные слова:', *root_words)

single_root_words()