import logging
from typing import Any, Dict
from .db.session import SessionLocal, engine
from .db.models import ETLResult, Base
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)

class ETLProcessor:
    @staticmethod
    def extract() -> int:
        import random
        value = random.randint(0, 100)
        logger.info('Extracted value %s', value)
        return value

    @staticmethod
    def transform(value: int) -> Dict[str, Any]:
        result = {'original': value, 'doubled': value*2}
        logger.info('Transform result %s', result)
        return result

    @staticmethod
    def persist_result(dag_id: str, task_id: str, run_id: str, payload: Dict[str, Any], status: str = 'SUCCESS'):
        """Write ETLResult to Postgres using SQLAlchemy session"""
        db = SessionLocal()
        logger.info(f'TODO DB: {db}')
        try:
            rec = ETLResult(dag_id=dag_id,
                            task_id=task_id,
                            run_id=run_id,
                            payload=payload,
                            status=status
                            )
            db.add(rec)
            db.commit()
            db.refresh(rec)
            logger.info('Persisted ETLResult id=%s', rec.id)
            return rec.id

        except SQLAlchemyError as ex:
            db.rollback()
            logger.exception('DB error while persisting result')
            raise

        finally:
            db.close()

    @staticmethod
    def ensure_tables():
        """Call once to create tables - useful in init or migrations."""
        Base.metadata.create_all(engine) # 若不存在，則建立表格
        from lib.db.models import ETLResult