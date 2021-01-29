'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''

min_salory = []
middle_salory = 0
i = 0
with open('workers_salary.txt', 'r') as f:
    for lines in f:
        i += 1
        line = lines.split(' ')
        middle_salory += int(line[1])

        if line[1] < str(20000):
            min_salory.append(line[0])

    middle_salory = middle_salory / i

    print(f'Средний оклад = {middle_salory}')
    print(f'Оклад менее 20 тыс. {min_salory}')
