'''Простой анализатор текста, функционал можно увеличить в зависимости от требований к программе, например добавить считывание с файла'''
from collections import Counter

txt = input('Введите ваш текст: ')

count_symbols = len(txt)
count_word = len(txt.split())
count_sentences = len(txt.split('.'))
count_words = Counter(txt.replace(r'!()-[]{};?@#$%:\,./^&amp;*', '').split())
print(f'Количество символов: {count_symbols}\nКоличество слов: {count_word}\nКоличество предложений: {count_sentences}')
for key in count_words:
    print(f'{key} : {count_words[key]}')