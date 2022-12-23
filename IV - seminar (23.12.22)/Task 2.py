# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def SimpleMultiplicities(n):
    i = 2
    lst = []
    while i <= n + 1:
        if n % i == 0:
            n = n // i
            lst.append(i)
        else:
            i += 1
    return lst


N = int(input("Введите число, которое необходимо разложить на простые множетиле "))
myLst = SimpleMultiplicities(N)
print(*myLst, sep="*")
