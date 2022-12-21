# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

N = int(input())
notlst = [1, -1]
a = 1
b = -1
for i in range(3, N + 1):
    c = a - b
    notlst.append(c)
    a = b
    b = c
lst = notlst[::-1]
lst.append(0)
lst.append(1)
lst.append(1)
a = 1
b = 1
for i in range(3, N + 1):
    c = a + b
    lst.append(c)
    a = b
    b = c
print(lst)
