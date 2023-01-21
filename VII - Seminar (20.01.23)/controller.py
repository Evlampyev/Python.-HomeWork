import interface
import model
import logger


def project_launch():
    # interface.html_creator()
    data_list = interface.input_data()
    data_str = model.unification(data_list)
    logger.log_data(data_str)
    logger.log_data_list(data_list)
