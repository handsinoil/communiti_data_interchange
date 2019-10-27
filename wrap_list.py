"""Смысл в том чтобы использовать структуру данных лист, для того чтобы с консоли человек вводит данные, эти данные
записываются в общую ведомость, следующий человек вводит свои данные, они суммируются с предыдущим и обновляются,
и так далее для всех членов сообщества"""

# TODO
# Выберем список как структуру данных где 0 позиция это будет имя Члена сообщества
from typing import List
product1 = 0
product2 = 0
product3 = 0

list_temp = ['name', 'product1', 'product2', 'product3']
list_sum = []
list_tab =[]
list_member = []
# ввести кол-во членов сообщества
amount_com = 3
for i in range(amount_com):
    list_member.append(input('участник введите через запятую свое имя, и кол-во продуктов необходимое'
                             ' пример: Вася, 5, 6, 3 = ')
                       )
for j in list_member:
    list_d = [k.strip() for k in j.split(',')]
    list_tab.append(list_d)
    #получили список списков
#надо все сложить и распечатать результаты
for s in list_tab:
    product1 += int(s[1])
    product2 += int(s[2])
    product3 += int(s[3])
print('план производства: \n'
      ' product1: ', product1, '\n',
      'product2: ', product2, '\n',
      'product3: ', product3, '\n',)
