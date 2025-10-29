import os, sys
# [1] 獲取當前 DAG 檔案的目錄 (即 /opt/airflow/dags)
# [2] 獲取 DAG 目錄的父目錄 (即 /opt/airflow/)
# [3] 將父目錄加入到 Python 搜尋路徑中，這樣就能找到 lib/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup

from lib.etl_processor import ETLProcessor

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=3),
    'on_failure_callback': None,
}

with DAG(
    dag_id='etl_branch_xcom_demo',
    default_args=default_args,
    schedule_interval='0 2 * * *', # daily at 2am
    start_date=days_ago(1),
    catchup=False,
    max_active_runs=1,
) as dag:

    def _extract(**kwargs):
        value = ETLProcessor.extract()
        kwargs['ti'].xcom_push(key='value',
                               value=value)
        return value

    def _branch(**kwargs):
        ti = kwargs['ti']
        value = ti.xcom_pull(task_ids='extract',
                             key='value')
        if value is None:
            return 'alert'
        return 'transform' if int(value) > 50 else 'alert'

    def _transform(**kwargs):
        ti = kwargs['ti']
        value = ti.xcom_pull(task_ids='extract',
                             key='value')

        result = ETLProcessor.transform(int(value))
        dag_id = kwargs['dag'].dag_id
        run_id = kwargs.get('run_id')

        ETLProcessor.persist_result(dag_id=dag_id,
                                    task_id='transform',
                                    run_id=run_id,
                                    payload=result,
                                    status='SUCCESS')
        ti.xcom_push(key='result',
                     value=result)

        return result

    def _alert(**kwargs):
        ti = kwargs['ti']
        value = ti.xcom_pull(task_ids='extract', key='value')

        ETLProcessor.persist_result(dag_id=kwargs['dag'].dag_id,
                                    task_id='alert',
                                    run_id=kwargs.get('run_id'),
                                    payload={'value': value},
                                    status='ALERT')

    start = EmptyOperator(
        task_id='start'
    )
    extract = PythonOperator(
        task_id='extract',
        python_callable=_extract,
        provide_context=True
    )
    branch = BranchPythonOperator(
        task_id='branch',
        python_callable=_branch,
        provide_context=True
    )
    transform = PythonOperator(
        task_id='transform',
        python_callable=_transform,
        provide_context=True
    )
    alert = PythonOperator(
        task_id='alert',
        python_callable=_alert,
        provide_context=True
    )
    end = EmptyOperator(
        task_id='end',
        trigger_rule='none_failed_min_one_success'
    )

    start >> extract >> branch >> [transform, alert] >> end