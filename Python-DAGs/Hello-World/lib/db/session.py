import os, logging, pathlib
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)

current_dir = pathlib.Path(__file__).parent.parent
env_path = current_dir.parent / '.env'
load_dotenv(dotenv_path=env_path)
logger.info(f"\ncurrent_dir: {current_dir}")
logger.info(f"env_path: {env_path}\n")

db_url = os.getenv(
        'ETL_DB_URL',
        'postgresql+psycopg2://airflow:airflow@postgres/etl_data'
)
try:
    if not database_exists(db_url):
        logger.warning(f"Creating missing database: {db_url}")
        create_database(db_url)
    else:
        logger.info("✅ Database already exists.")

except OperationalError as e:
    logger.error(f"❌ Cannot connect to Postgres server: {e}")
    raise

engine = create_engine(db_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)