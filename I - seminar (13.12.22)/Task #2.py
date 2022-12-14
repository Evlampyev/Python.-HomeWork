# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print("I quarter")
elif (x > 0 and y < 0):
    print("IV quarter")
elif x < 0 and y > 0:
    print("II quarter")
else:
    print("III quarter")

# по условию задачи "причём X ≠ 0 и Y ≠ 0" значит не может лежать на оси