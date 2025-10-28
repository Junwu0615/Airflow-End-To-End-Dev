from sqlalchemy import Column, Integer, String, DateTime, JSON, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ETLResult(Base):
    __tablename__ = 'etl_results'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dag_id = Column(String(128), nullable=False)
    task_id = Column(String(128), nullable=False)
    run_id = Column(String(128), nullable=True)
    executed_at = Column(DateTime(timezone=True), server_default=func.now())
    payload = Column(JSON, nullable=True)
    status = Column(String(32), nullable=False, default='SUCCESS')

    def __repr__(self):
        return f'<ETLResult id={self.id} dag={self.dag_id} task={self.task_id} status={self.status}>'