# Задача "Однокоренные"
def single_root_words(*other_words, root_words = 'rich'):
    same_words = []
    for i in other_words:
        if root_words.upper() in i.upper():
            same_words.append(i)

    return print(same_words)

result1 = single_root_words( 'rich', 'richiest', 'orichalcum', 'cheers', 'richies')

