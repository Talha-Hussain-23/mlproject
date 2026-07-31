# What is Logger?

# A Logger records everything that happens in your program.

# Think of it as a diary or CCTV camera.

# It writes:

# When the program starts.
# When data is loaded.
# When model training starts.
# When the model is saved.
# If an error occurs.
# Why do we use Logger?

# Without Logger:

# Program crashed.

# ❌ Don't know where.
# ❌ Don't know when.
# ❌ Don't know why.

# With Logger:

# 10:00 Data Ingestion Started

# 10:01 Data Loaded Successfully

# 10:03 Model Training Started

# 10:05 Error: customer.csv not found

# Now you know exactly what happened.

# Real Life Example

# Imagine you're a teacher.

# Attendance Register:

# 09:00 Ali Present

# 09:01 Ahmed Present

# 09:02 Sara Present

# That register is a log file.

# Logger Flow
# Program Starts
#       │
#       ▼
# Logger Creates Log File
#       │
#       ▼
# Program Runs
#       │
#       ▼
# Logger Writes Every Important Event
#       │
#       ▼
# Developer Reads Log

import logging
import os
from datetime import datetime
import sys

from src.exception import CustomException


LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs")

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)


# if __name__ == "__main__":

#     try:

#         logging.info("Logger has started.")

#         logging.info("Testing exception...")

#         x = 10 / 10     # Force an error

#         logging.info("This line will never execute.")

#     except Exception as e:

#         logging.error(f"An error occurred: {e}", exc_info=True)

#         raise CustomException(e, sys)