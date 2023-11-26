import logging
import os
import datetime

from config import *
from reddit import get_tickers_and_comments



log = logging.getLogger()


def logging_handler():
    print('in logging_handler')
    log_directory = NEWSLETTER_LOG_PATH

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    log_format = '%(asctime)s %(levelname)s %(module)s:%(lineno)d %(message)s'

    # set up constant stream of logs so logs are wrtten as they are hit in the script
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(log_format))
    logging.getLogger().addHandler(stream_handler)

    log_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f'{log_directory}log-{log_name}.log'
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter(log_format))
    logging.getLogger().addHandler(file_handler)

    logging.getLogger().setLevel(logging.DEBUG)




def main():
    print("in main method")

    logging_handler()

    log.info(f"Started script at {datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")


    get_tickers_and_comments(log)


if __name__ == '__main__':
    main()
