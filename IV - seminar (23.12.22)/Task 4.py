# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5
# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
#     a, b, c, d, e, h - рандом
import random

k = int(input("Введите степень k "))

lst = []
for i in range(k + 1):
    lst.append(random.randint(0, 100))
print("Коэффициенты: ", *lst)
for i in range(k):
    if lst[i] > 0:
        print(str(lst[i]) + 'x', end="")
        if k - i == 1:
            print(' + ', end="")
        else:
            print('^' + str(k - i) + ' + ', end="")
if lst[k] > 0:
    print(str(lst[k]))
