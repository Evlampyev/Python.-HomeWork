# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в одном текстовом файле, в котором строка.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Восстановить
# Ввёл: stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"
# Реализовать алгоритм в обе стороны, сначала сжимаем, потом разжимаем, работаем только со строками

def compression(stroka):
    RLE = str()
    simv = stroka[0]
    numberOfCharacters = 1
    for i in range(1, len(stroka)):
        if stroka[i] == simv:
            numberOfCharacters += 1
        else:
            if numberOfCharacters > 1:
                RLE = RLE + str(numberOfCharacters) + simv
            else:
                RLE += simv
            numberOfCharacters = 1
            simv = stroka[i]
    if numberOfCharacters == 1:
        RLE += simv
    else:
        RLE += str(numberOfCharacters) + simv
    return RLE


def unarchive(stroka):
    unRLE = str()
    for i in range(len(stroka)):
        temp = stroka[i]
        if temp.isdigit():
            k = int(stroka[i])
            i += 1
            for z in range(k - 1):
                unRLE += stroka[i]
        else:
            unRLE += stroka[i]
    return unRLE


with open('data.txt', 'r') as f:
    data = f.read()
print("Исходное состояние", data)
compress = compression(data)
print("После применения алгоритма RLE:", compress)
uncompress = unarchive(compress)
print("Исходное значение:", uncompress)
