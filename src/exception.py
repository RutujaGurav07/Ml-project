import sys 
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exe_tb = error_detail.exc_info()
    file_name =exe_tb.tb_frame.f_code.co_filename
    error_message = f"Error occur in python script [{file_name}] line number [{exe_tb.tb_lineno}] error message [{str(error)}]."

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
