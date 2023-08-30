from airflow import DAG
from airflow.decorators import task,dag
from datetime import datetime, timedelta
import pymssql
from decouple import config
from airflow.providers.google.cloud.transfers.mssql_to_gcs import MSSQLToGCSOperator

default_args = {
    "start_date": datetime(2023, 8, 30)
}

@dag(
    schedule=None,
    default_args=default_args,
    tags = 'retail',
    catchup=False, dagrun_timeout=timedelta(minutes=10), max_active_tasks=2, max_active_runs=1
    )

def retail():
    upload_sql_stat = MSSQLToGCSOperator(
    task_id = 'upload_sql_stat',
    sql=config('sql'),
    bucket=config("bucket"),
    filename="raw/imdb.csv",
    gcp_conn_id="conn_id",
    mssql_conn_id="sql_connid",
    export_format="csv"
)
retail()

def connector():

    @task(task_id='sql_conn')
    def sql_conn():
        conn = pymssql.connect(
            server=config('server'),
            user=config('user'),
            password=config('password'),
            database=config('database')    
            )
        
        schema = config("schema")
        query1 = f"""
            select Top 10 * from {schema}
                 """
        cursor = conn.cursor()
        queryresult  = cursor.execute(query1)
        records = cursor.fetchall()
        for r in records:
            pass
    
    sql_conn()

connector()
