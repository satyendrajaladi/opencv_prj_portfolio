import logging
from pathlib import Path

from config import OUTPUT_FOLDER


LOG_FILE = Path(OUTPUT_FOLDER) / "detector.log"


def save_log(*args):
    if not args:
        raise ValueError("At least one value is required to create a log entry.")

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    log_file = LOG_FILE.resolve()
    logger = logging.getLogger("license_plate_detector")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not any(
        isinstance(handler, logging.FileHandler)
        and Path(handler.baseFilename) == log_file
        for handler in logger.handlers
    ):
        handler = logging.FileHandler(log_file, encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)

    logger.info(" ".join(str(arg) for arg in args))
