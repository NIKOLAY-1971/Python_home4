# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степеь полинома: '))
lst = []
lstNew = []
for i in range(k+1):
    lst.append(random.randint(0, 100))
print('Список коэффициентов многочлена:')
print(lst)
for i in lst:
    if i:
        if k == 0:
            variable = ''
        elif k == 1:
            variable = 'x'
        else:
            variable = f'x^{k}'
        variable_k = f'{i}{variable}'
        lstNew.append(variable_k)
    k = k-1
polinom = '+'.join(lstNew)+'=0'
print(polinom)

with open('file.txt', 'w') as data:
    data.write(polinom)
data.close()
