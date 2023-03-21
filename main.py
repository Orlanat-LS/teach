# # import os
# #
# # target_dir = r'C:\test'
# #
# #
# # for path, dirs, files in os.walk(target_dir):
# #     print(path, dirs, files)
# #     if path == target_dir:
# #         continue
# #     for f in files:
# #         print(path)
# #         print(path.replace(target_dir, ''))
# #         print(path.replace(target_dir, '').replace('\\', '_'))
# #         n_path = path[len(target_dir) + 1:].replace('\\', '_')
# #
# #         # os.rename(f'{path}\\{f}', f"{target_dir}\\{n_path}_{f}")
# #
# # # import shutil
# # # for e in os.listdir(target_dir):
# # #     full_path = f'{target_dir}\\{e}'
# # #     if os.path.isdir(full_path):
# # #         shutil.rmtree(full_path)
#
# from collections import Counter
#
# stringsplit = open('book.txt').read().split()
#
# dictionary = []
# for word in stringsplit:
#     print(Counter(word))
#     dictionary.append(Counter(word))
#
# dictionary_index = 0
# dictionary_len = 0
# index = 0
# ch = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')
# k = ''
# v = ''
#
# for e in dictionary:
#     cnt = 0
#     for key, value in e.items():
#         if key in ch:
#             cnt += 1
#
#     if cnt == 1 and len(stringsplit[index]) > dictionary_len:
#         dictionary_len = len(stringsplit[index])
#         dictionary_index = index
#     index += 1
#
# for key, value in dictionary[dictionary_index].items():
#     if key in ch:
#         k = key
#         v = value
#
# print(f'Самое длинное слово --> {stringsplit[dictionary_index]} <--,')
# print(f'в котором --> {len(stringsplit[dictionary_index])} <-- символов и')
# print(f'единственная глассная буква --> {k} <--, которая повторяется {v} раз(а)')
#
# import flask

import json

l = list()
for i in range(10):
    l.append(i)

l.append({1: 123, 'qwe': 'asdasd'})

# with open('test.json', 'w') as f:
#     json.dump(l, f, indent='\t' )

with open('test.json', 'r') as fp:
    x = json.load(fp)
    print(type(x))

