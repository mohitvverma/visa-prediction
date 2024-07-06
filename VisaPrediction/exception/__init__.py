import sys


def error_detail_message(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"""Error occurred while processing file name :{file_name}, Line No: {exc_tb.tb_lineno},
                        Error :{str(error)}"""

    return error_message


class VisaException(Exception):
    def __init__(self, error_message, error_details):
        """
        :param self:
        :param error_message: Error message in string format
        :param error_details:
        :return:
        """
        super.__init__(error_message)
        self.error_message = error_detail_message(
            error_message, error_details=error_details
        )

    def __str__(self):
        return self.error_message
