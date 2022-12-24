# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# 2*x^  + 4*x      5*x^2 + 2*x
#     7x^2 + 6x

def Change(st):
    k = max(st.find('x-'), st.find('x+'))
    if k > 0:
        st = st[:(k + 1)] + '^1' + st[(k + 1):]
    return st


def StringInList(s, m):
    number = ""
    lst = [0 for i in range(m + 1)]
    arg = ""
    znak = 1 if s[0] == '-' else 2
    for i in range(0, len(s)):
        if s[i].isdigit():
            number += s[i]
        elif s[i] == 'x':
            arg = number
            number = ""
        elif s[i] == '+':
            lst[int(number)] = int(arg) * (-1) ** znak
            znak = 2
            number = ""
        elif s[i] == '-':
            lst[int(number)] = int(arg) * (-1) ** znak
            znak = 1
            number = ""
    lst[0] = int(number) * (-1) ** znak
    return lst


def TotalList(sl1, sl2, m):
    total = [0] * (m + 1)
    for i in range(0, m + 1):
        total[i] = sl1[i] + sl2[i]
    return total


def PrintList(lst):
    l = len(lst) - 1
    while lst[l] == 0:
        l -= 1
    print(lst[l], 'x^', l, sep="", end="")
    for i in range(l - 1, -1, -1):
        if lst[i] > 0:
            print(' +', lst[i], sep="", end="")
            if i >= 2:
                print('x^', i, sep="", end="")
            elif i == 1:
                print('x', end="")
        elif lst[i] < 0:
            print(' ', lst[i], sep="", end="")
            if i >= 2:
                print('x^', i, sep="", end="")
            elif i == 1:
                print('x', end="")


data1 = open('1.txt', 'r')
data2 = open('2.txt', 'r')
m1 = str(data1.readline())
m2 = str(data2.readline())
data1.close()
data2.close()

print(m1, " + ", m2, " = ", end="")
m1 = Change(m1)
m2 = Change(m2)

maxStep1 = int(m1[m1.index('^') + 1])
maxStep2 = int(m1[m1.index('^') + 1])
maxStep = max(maxStep2, maxStep1)

ls1 = StringInList(m1, maxStep)
ls2 = StringInList(m2, maxStep)

tot = TotalList(ls1, ls2, maxStep)
# print("I - ", ls1)
# print("II - ", ls2)
# print("I + II = ", tot)

PrintList(tot)


# Работает только с однозначными степенями х и с обязательным наличием свободного члена
