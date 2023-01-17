# Создайте программу для игры в ""Крестики-нолики"".
# ввод имени, проверять что не установили в занятую клетку
# результат кто выиграл или ничья
# выводить результат как выглядит доска после каждого хода

def InputPole(key: int = 3):
    pol = []
    for i in range(3):
        pol = [['.'] * key for i in range(key)]
    return pol


def PrintPole(pol, key: int = 3):
    print("   ", 0, 1, 2)
    print("   ", "|", "|", "|")
    a = 0
    for i in pol:
        print(a, '-', ' '.join(list(map(str, i))))
        a += 1


def СheckingWinner(pol, key: int = 3):
    win = str()
    for i in range(3):
        if pol[i][0] == pol[i][1] == pol[i][2] and pol[i][0] != '.':
            win = pol[i][0]
            break
        if pol[0][i] == pol[1][i] == pol[2][i] and pol[0][i] != '.':
            win = pol[0][i]
            break
    if pol[0][0] == pol[1][1] == pol[2][2] and pol[0][0] != '.':
        win = pol[0][0]
    if pol[0][2] == pol[1][1] == pol[2][0] and pol[0][2] != '.':
        win = pol[0][2]
    return win


playingField = InputPole()
print("Поле для игры в крестики - нолики ")
print("Точками указаны свободные клетки")
PrintPole(playingField)
victory = False

whoseMove = 0  # 0 - Это нолик, 1 - это крестик
move = ['Нолик', 'Крестик']
motion = ['o', 'x']
winner = str()
noMoves = 0
print("Для хода необходимо указать через пробел номер столбца и номер строки. Удачи!")
while winner == "" and noMoves < 9:
    print('Ходит', move[whoseMove])
    x, y = map(int, input().split())
    while playingField[y][x] == 'o' or playingField[y][x] == 'x':
        x, y = map(int, input("Эта клетка занята, повторите ввод: ").split())
    playingField[y][x] = motion[whoseMove]
    noMoves += 1
    print('______________________________________')
    PrintPole(playingField)
    winner = СheckingWinner(playingField)
    whoseMove = (whoseMove + 1) % 2
if winner == "" and noMoves == 9:
    print("Ничья")
else:
    print("Победил ", winner)
