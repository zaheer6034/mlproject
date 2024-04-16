import sys

def error_message_details(error, error_detail: sys):
    # Custom exception handling. This will give us the error details
    _,_, exc_tb = error_detail.exc_info() 
    
    file_name = exc_tb.tb_frame.f_code.co_filename


    error_message = "Error occured in python script [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


# Custom exception class inherting from Exception
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        
        # Function to raise/print the exception

        return self.error_message
    