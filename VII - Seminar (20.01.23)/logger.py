from datetime import datetime as dt


def log_data(data):  # в одну строку складываем
    time = dt.now()
    with open('log.csv', 'a') as file:
        file.write('{}, {} \n'
                   .format(time, data))


def log_data_list(data_list):  # перечисление в несколько строк
    time = dt.now()
    with open('log_list.csv', 'a') as file:
        file.write('-------------- \n')
        for record in data_list:
            file.write('{} \n'
                       .format(record))
