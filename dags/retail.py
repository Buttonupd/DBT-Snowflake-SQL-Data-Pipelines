import json
from airflow.models.connection import Connection
import pandas as pd
from pathlib import Path
from airflow import DAG
from airflow.operators.python import PythonOperator,BranchPythonOperator
from airflow.decorators import task,dag
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator
import time
from datetime import datetime, timedelta
import pymssql
from decouple import config

default_args = {
    "start_date": datetime(2023, 8, 30)
}


@dag(
    schedule="@daily",
    default_args=default_args,
    catchup=False, dagrun_timeout=timedelta(minutes=10), max_active_tasks=2, max_active_runs=1
    )

def my_dag():
    @task(task_id='testsql')
    def test_sql():
    

        conn = pymssql.connect(
            server=config('server'),
            user=config('user'),
            password=config('password'),
            database=config('database')
            
    )
        
     
        query1 = "select Top 100 * from TestData"
        print(query1)
        print(conn)
        cursor = conn.cursor()
        queryresult  = cursor.execute(query1)

        print(queryresult)
    
    test_sql()
my_dag()
