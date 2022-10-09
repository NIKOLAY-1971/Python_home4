# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random


n = int(input('Задайте размерность списка:'))
lst = []
lstNew = []
for i in range(n):
    lst.append(random.randint(1, n))
print('Исходный список:')
print(lst)
for i in lst:
    if lst.count(i) < 2:
        lstNew.append(i)
print('Список с неповторяющимися элементами')
print(lstNew)
