def line_print(liner):
    count = liner.find(',')
    print(f'{liner[count + 1:-1]:45} - запись добавлена: {liner[:count]}')


def data_print():
    with open('log.csv', 'r') as file:
        lines = file.readlines()
    for line in lines:
        line_print(line)
