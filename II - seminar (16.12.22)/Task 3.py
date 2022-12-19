# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]
from random import *

N = int(input("Введите значение N: "))
array = [randint(-N, N) for i in range(2 * N + 1)]
print(array)
index = []
composition = 1  # итоговое произведение
i = 0
while i < 5:
    number = int(input(f'Введите {i + 1}-ый индекс '))
    if 2 * N + 1 > number >= 0:
        index.append(number)
        composition *= array[index[i]]
        i += 1
    else:
        print("не верный индекс")
print(f'Произведение элементов на {index} местах = {composition}')
