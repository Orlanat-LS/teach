from collections import Counter

stringsplit = open('book.txt').read().split()

dictionary = []
for word in stringsplit:
    dictionary.append(Counter(word))

dictionary_index = 0
dictionary_len = 0
index = 0
ch = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')
l = 0
for e in dictionary:
    cnt = 0
    for key, value in e.items():
        if key in ch:
            cnt += 1

    # if cnt == 1 and len(stringsplit[index]) > dictionary_len:
    #     dictionary_len = len(stringsplit[index])
    #     dictionary_index = index
    if cnt > l and len(stringsplit[index]) >= dictionary_len:
        dictionary_len = len(stringsplit[index])
        dictionary_index = index
        l = cnt
    index += 1

for key, value in dictionary[dictionary_index].items():
    if key in ch:
        print(f'Самое длинное слово --> {stringsplit[dictionary_index]} <--,')
        print(f'в котором --> {len(stringsplit[dictionary_index])} <-- символов и')
        print(f'в котором --> {l} <-- уникальных гласных символов')
        # print(f'единственная глассная буква --> {key} <--, которая повторяется {value} раз(а)')
        break
