# Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

lst = [12, 'sadf', 5643]
digit = list(filter(lambda x: type(x) == int, lst))
str = list(filter(lambda x: not type(x) == int, lst))

print(f"Было: {lst}")
print(f"Стало: {str}, {digit}")
