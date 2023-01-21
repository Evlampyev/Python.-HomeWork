import interface
import model
import logger
import view


def project_launch():
    s = 2
    while s != 0:
        # interface.html_creator()
        if s == 1:
            add_entry()
        else:
            view.data_print()


def add_entry():
    data_list = interface.input_data()
    data_str = model.unification(data_list)
    logger.log_data(data_str)
    logger.log_data_list(data_list)
    return
