import interface
import model
import logger
import view


def project_launch():
    s = interface.select_action()
    while s != 0:
        if s == 1:
            view.data_print()
        else:
            add_entry()
        s = interface.select_action()



def add_entry():
    data_list = interface.input_data()
    data_str = model.unification(data_list)
    logger.log_data(data_str)
    logger.log_data_list(data_list)
    return
