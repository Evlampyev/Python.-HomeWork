# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

length = int(input("Введите размер списка "))
lst = [random.randint(1, 10) for i in range(length)]
print(lst)
rez = []
for i in range(0, length // 2 + length % 2):
    rez.append(lst[i] * lst[length - i - 1])
print(rez)
