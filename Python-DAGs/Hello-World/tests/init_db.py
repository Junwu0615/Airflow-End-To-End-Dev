import logging
from lib.etl_processor import ETLProcessor

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)

ETLProcessor.ensure_tables()
logger.warning('Tables created !')