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
import pyodbc


default_args = {
    "start_date": datetime(2022, 1, 1)
}


@dag(
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False, dagrun_timeout=timedelta(minutes=10), concurrency=2, max_active_runs=1
    )

def my_dag():
    @task(task_id='testsql')
    def test_sql():
        server="DKARIUKI-PC\BASESSQL_SERVER"
        username="sa"
        password="Saf3rthanc0v1d19"
        database="master"
        ddw_connection = pyodbc.connect('sql_connid')
        query1 = "select 1"
        print(query1)
        print(ddw_connection)
        cursor = ddw_connection.cursor()
        queryresult  = cursor.execute(query1)
   ##database_names    = [db.ddw_databasename for db in databases_to_sync]
        print(queryresult)
    
    test_sql()
my_dag()