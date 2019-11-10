from collections import namedtuple
lst=[]
n = input('введите кол-во участников:_')
for i in range(int(n)):
    name = input('введите имя: ')
    product1 = input('product1 введите кол-во кг: ')
    product2 = input('product2 введите кол-во кг: ')
    name_plan = namedtuple(name, 'product1, product2')
    p = name_plan(product1=product1, product2=product2)
    lst.append(p)

s1=0
s2 =0
for j in lst:
    s1 += int(j.product1)
    s2 += int(j.product2)
pl = namedtuple('ob_plan', 'product1, product2')
plan = pl(product1=s1, product2=s2)

print(plan)
