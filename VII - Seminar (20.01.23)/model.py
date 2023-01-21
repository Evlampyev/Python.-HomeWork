record = {
    0: 'Фамилия',
    1: 'Имя',
    2: 'Номер телефона',
    3: 'Должность'
}


def unification(data_list):
    data = str()
    for i in range(len(data_list)):
        data = data + data_list[i] + ' ,' if i <= 2 else data + data_list[i]
    return data
