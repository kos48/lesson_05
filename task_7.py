'''7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.'''

import re, json

average_profit =0
kol = 0
profit_dict = {}
final_list = []

with open('text_task_7.txt', 'r') as f:
    for lines in f:
        firm_name = (lines.split(' ')[0]) # название фирмы
        proceeds = int((re.findall(r'\d+', lines)[1])) #выручка
        costs = int((re.findall(r'\d+', lines)[2])) # издержки
        profit = proceeds - costs # прибыль
        profit_dict.update([(firm_name, profit)]) # упаковываем в словарь

        if profit > 0:
            kol += 1
            average_profit += profit

    average_profit = average_profit / kol # средняя прибыль
    final_list.append(profit_dict)
    final_list.append(dict([('average_profit', average_profit)]))
    print(final_list)

with open('text_task_7.json', 'w', encoding='utf-8') as f:
    json_final_list = json.dump(final_list, f)
