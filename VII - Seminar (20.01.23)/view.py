def line_print(liner):
    count = liner.find(',')
    print('{} - запись добавлена: {}'.format(liner[count+1:], liner[:count]))


def data_print():
    with open('log.csv', 'r') as file:
        lines = file.readlines()
    for line in lines:
        line_print(line)
