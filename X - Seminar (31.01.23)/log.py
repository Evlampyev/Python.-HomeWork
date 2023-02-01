from datetime import datetime


def logging(id, task):
    now = datetime.now()
    with open('log.scv', 'a') as file:
        text = str(now) + "--" + str(id) + " " + task + '\n'
        file.write(text)
