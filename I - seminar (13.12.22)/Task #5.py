# (!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

X = [0, 1]
Y = [0, 1]
Z = [0, 1]
count = 0
for x in X:
    for y in Y:
        for z in Z:
            print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} ", end=" ")
            if (not (x or y or z)) == (not (x) and not (y) and not (z)):
                print(True)
                count += 1
            else:
                print(False)
if count == 8:
    print("Выражение истинно при любых значениях переменных")
