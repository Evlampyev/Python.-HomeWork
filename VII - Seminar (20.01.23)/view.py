def line_print(liner):
    print(liner)


def data_print():
    with open('log.csv', 'r') as file:
        lines = file.readlines()
    for line in lines:
        line_print(line)
