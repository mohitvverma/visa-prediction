import sys
import os

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"""Error occurred while processing file name :{file_name}, Line No: {exc_tb.tb_lineno},
                        Error :{str(error)}."""

    return error_message


class VisaException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param self:
        :param error_message: Error message in string format
        :param error_details:
        :return:
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
