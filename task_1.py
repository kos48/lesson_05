'''1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

with open('user_data.txt','+w',encoding='utf-8') as f:
    flag = ''
    num_line = 1

    while flag != 'exit':
        text = input(f'введите {num_line} строку. Пустая строка - выход: ')
        if text == '':
            flag = 'exit'
        f.write(text + '\n')
        num_line += 1

