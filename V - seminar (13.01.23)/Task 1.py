# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит не больше 120 конфет. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет (необходимо проверять).
# Победитель - тот, кто оставил на столе 0 конфет.  Бот берет случайное число от 1 до 28.
# a) Добавьте игру против бота
# # Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)
import random

totalSweet = int(input('Исходное количество конфет: '))
player = ['Человек', 'бот']
numPl = 0
victory = -1
while totalSweet > 0:
    print('Ходит ', player[numPl], ':', end="")
    if numPl == 1:
        tookItAway = random.randint(1, 28)
        if tookItAway >= totalSweet:
            tookItAway = totalSweet
        print(tookItAway)
        numPl = (numPl + 1) % 2
        if totalSweet - tookItAway <= 0:
            victory = 1
    else:
        tookItAway = int(input())
        while (tookItAway <= 0 | tookItAway > 28):
            print("Некорректный ввод, повторите ")
            tookItAway = int(input())
        numPl = (numPl + 1) % 2
        if totalSweet - tookItAway <= 0:
            victory = 0
    totalSweet -= tookItAway
    print("Осталось", totalSweet, 'конфет')
print("победитель:", player[victory])
