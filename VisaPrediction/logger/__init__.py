
import logging
import os
import sys
from datetime import datetime

"""
We need four things in our logging file
1. File name should created as the logger will run multiple times.
2. Setup the where the logging folder will be created.
3. Setup the path for logging files creating multiple files within the logger folder.
"""



LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

main_file_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.insert(0, main_file_path)

logs_path = os.path.join(main_file_path,
                         'Logs_data',
                         LOG_FILE_NAME)


if not os.path.exists(logs_path):
    os.makedirs(logs_path, exist_ok=True)



LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE_NAME)


logging.basicConfig(

    filename = LOG_FILE_PATH,


    format ="[ %(asctime)s ] %(name)s  %(lineno)d - %(filename)s s- %(levelname)s %(message)s",
    level = logging.DEBUG
    )


def main():
    try:
        3/0
    except Exception as e:
        logging.exception(e, exc_info=True)
        logging.error(e)


if __name__ == '__main__':
    main()