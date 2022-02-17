import logging.config
import os
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/logs/app.log", "a", "utf-8"),
        logging.StreamHandler()
    ],
)
logger = logging.getLogger(__name__)
logger.info("Logger initialized...")
