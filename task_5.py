'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

from functools import reduce


def sum_func(num_1, num_2):
    return int(num_1) + int(num_2)


with open('text_task_5.txt', '+w', encoding='utf-8') as f:
    f.write('1 2 3 4 5 6')

with open('text_task_5.txt', 'r', encoding='utf-8') as f:
    text = f.readline()
    result = reduce(sum_func, (text.split(' ')))
    print(f'Сумма чисел в файле = {result}')
