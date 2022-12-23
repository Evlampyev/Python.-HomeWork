# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1

def VariousElements(lst):
    Set = set()
    for i in lst:
        if lst.count(i) == 1:
            Set.add(i)
    return Set


myLst = []
for i in range(int(input("Укажите количество чисел в последовательности "))):
    myLst.append(int(input()))
print("Ввод: ", end="")
print(*myLst)
mySet = VariousElements(myLst)
print("Вывод: ", end="")
print(*mySet)
