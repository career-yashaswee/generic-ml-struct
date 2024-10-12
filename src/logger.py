import logging
import os
from datetime import datetime

LOGFILE = f"{os.path.dirname(__file__)}/logs/{datetime.now().strftime('%Y%m%d')}.log"
logs_path = os.path.dirname(LOGFILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOGFILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO
)