import logging 
from datetime import datetime
import os, sys

LOG_DIR="./logs"

CURRENT_TIME_STAMP= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR ,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
    filemode="w",
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s'
    ,level=logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE_PATH)
    ]
)

logger = logging.getLogger("IPYNBrenderer")