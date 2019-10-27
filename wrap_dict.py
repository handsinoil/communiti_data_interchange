from pprint import pprint
from typing import Dict

import input_mod

"""здесь используется словарь для упаковки данных"""
dict_data = dict.fromkeys(['помидор', 'огурец', 'картофель'], 0)
dict_data_name: Dict[str, str] = {}
dict_summary = dict.fromkeys(['помидор', 'огурец', 'картофель'], 0)
# dict_data = dict(помидор=0, огурец=0, картофель=0)

amount_com = 3  # ввод кол-ва участников

# заполнение данными
for i in range(amount_com):
    name = input('введите свое имя: ')

    input_mod.print_info()
    dict_data = input_mod.input_for_dict(**dict_data)
    dict_data_name[name] = dict_data
    # подсчет общего кол-ва
    for i in dict_summary.keys():
        dict_summary[i] += int(dict_data[i])
#вывод результатов
input_mod.output_for_dict(**dict_summary)



