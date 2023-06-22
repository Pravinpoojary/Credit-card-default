import sys
from src.logger import logging


def error_msg_det(error,error_det:sys):
    _,_,exc_tb = error_det.exc_info() # this will display 3 variables , but we need only one, hence_,_, is mentoned
    file_name=exc_tb.tb_frame.f_code.co_filename


    error_msg= "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_msg


class CustomException(Exception):
    
    def __init__(self,error_msg,error_det:sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_det(error_msg,error_det=error_det)

    def __str__(self):
        return self.error_msg


