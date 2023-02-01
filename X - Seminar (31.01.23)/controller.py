from models import str_to_list, operations



def solve_task(task):
    while task.find(')')>0:

    task = str_to_list(task)
    task = operations(task, 0)
    task = operations(task, 2)

    return task[0]
