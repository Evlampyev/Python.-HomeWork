import model


def input_data():
    data_list = []
    for i in range(4):
        data_list.append(input('Введите {}: '.format(model.record[i])))
    return data_list


def select_action():
    print("0. Выход")
    print("1. Вывести весь список")
    print("2. Добавить новую запись")
    sel = int(input("Что вы хотите сделать: "))
    return sel
