# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

N = int(input("Введите количество элементов "))
lst = [random.uniform(0, 10) for i in range(N)]
print(lst)
Min = 1
Max = 0
for i in range(0, N):
    if (lst[i] - lst[i] // 1) > Max:
        Max = lst[i] - lst[i] // 1
    if (lst[i] - lst[i] // 1) < Min:
        Min = lst[i] - lst[i] // 1
print(f"Δ (max-min) = {Max} - {Min} = {Max-Min}")


