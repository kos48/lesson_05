'''1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''


text='abrakadabra'
with open('test_2.txt','w') as f:
    f.write(text)
