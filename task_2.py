'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.'''

num_str = 0

with open('my_text.txt', 'r') as f:
    for line in f:
        num_str += 1
        words = len(line.split(' '))
        print(f'В строке {num_str} - {words} слов')

    print(f'В этом файле {num_str} строк')
