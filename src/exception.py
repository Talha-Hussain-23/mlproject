# Where is Exception Handling Used?
# Reading CSV files
# Loading models
# Database connections
# API requests
# File operations
# Saving models
# Predictions
# Data preprocessing
# 24. Why is Exception Handling Important?
# Prevents program crashes.
# Makes debugging easier.
# Provides meaningful error messages.
# Keeps applications more reliable.
# Standard practice in professional software and ML projects.
# Beginner Memory Trick 🎯
# try
# │
# ├── "Try this code."
# │
# ▼
# Error?
# │
# ├── No → Continue
# │
# └── Yes
#       │
#       ▼
# except
#       │
#       ▼
# Handle Error
#       │
#       ▼
# Logger writes it
#       │
#       ▼
# Developer fixes it

#  | Keyword   | Meaning                                        |
# | --------- | ---------------------------------------------- |
# | `try`     | Try to execute the code.                       |
# | `except`  | Handle the error if one occurs.                |
# | `else`    | Runs only if no error occurs.                  |
# | `finally` | Always runs, whether there is an error or not. |
# | `raise`   | Manually create or re-raise an exception.      |
# ..................................................................
import sys 
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

