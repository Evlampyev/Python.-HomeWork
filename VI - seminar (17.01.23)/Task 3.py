# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите любое число: ')
newnumber = list(filter(lambda x: x.isdigit(), number))
newnumber = list(map(int, newnumber))
print(sum(newnumber))
