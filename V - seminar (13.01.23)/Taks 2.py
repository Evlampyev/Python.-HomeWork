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
    for i in pol:
        print(' '.join(list(map(str, i))))


playingField = InputPole()
PrintPole(playingField)
