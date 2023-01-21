import model


def input_data():
    data_list = []
    for i in range(4):
        data_list.append(input('Введите {}: '.format(model.record[i])))
    return data_list
