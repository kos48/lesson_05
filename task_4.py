'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл.'''

new_f = open('new_text_task_4.txt', 'w')
new_f.close()

numrer_rus = ['Один', 'Два', 'Три', 'Четыре']
i = 0

with open('text_task_4.txt', 'r') as f:
    for lines in f:
        line = lines.split(' ')
        line[0] = numrer_rus[i]
        i += 1

        with open('new_text_task_4.txt', 'a', encoding='utf-8') as new_f:
            new_f.write(' '.join(line))
