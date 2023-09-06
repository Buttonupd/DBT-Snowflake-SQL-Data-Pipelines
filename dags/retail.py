from airflow import DAG
from airflow.decorators import task,dag
from datetime import datetime, timedelta
import pymssql
from decouple import config
from airflow.providers.google.cloud.transfers.mssql_to_gcs import MSSQLToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from astro import sql as aql
from astro.files import File
from astro.sql.table import Table,Metadata
from astro.constants import FileType
from include.dbt_to_dag import cosmos_config
from cosmos import DbtTaskGroup
from cosmos import RenderConfig
from cosmos import LoadMode
from airflow.models.baseoperator import chain

default_args = {
    "start_date": datetime(2023, 8, 30)
}

@dag(
    schedule="@daily",
    default_args=default_args,
    catchup=False,
    tags = ['sentiment_pipeline']
    )


def sentiment_pipeline():

    upload_sql_stat = MSSQLToGCSOperator(
    task_id = 'upload_sql_stat',
    sql=config('sql'),
    bucket=config("bucket"),
    filename="raw/imdb.csv",
    gcp_conn_id="conn_id",
    mssql_conn_id="sql_connid",
    export_format="csv"
    )

    create_imdb_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_imdb_dataset',
        dataset_id='imdb',
        gcp_conn_id='conn_id'

    )
    upload_idb_dataset = aql.load_file(
        task_id='upload_idb_dataset',
        input_file=File(
            'gs://daniel_online_retail/raw/imdb.csv',
            conn_id='conn_id',
            filetype=FileType.CSV
        ),
        output_table=Table(
            name='raw_imdb',
            conn_id='conn_id',
            metadata=Metadata(schema='imdb')
        ),
        use_native_support=False
    )


    @task.external_python(python='/usr/local/airflow/soda_env/bin/python')
    def check_load(scan_name='check_load',checks_path='sources'):
        from include.dbt_to_dag.soda.check_function import check
        return check(scan_name,checks_path)
    

    @task.external_python(python='/usr/local/airflow/soda_env/bin/python')
    def check_transform(scan_name='check_transform',checks_path='transform'):
        from include.dbt_to_dag.soda.check_function import check
        return check(scan_name,checks_path)
    
    @task(task_id='sqlconn')
    def sql_Conn():
        conn = pymssql.connect(
            server=config('server'),
            user=config('user'),
            password=config('password'),
            database=config('database')
            
    )
        schema = config('schema')
        queryStatement = f"""
                        select Top 10 * from {schema}
                        """
        cursor = conn.cursor()
        records  = cursor.execute(queryStatement)
        records = cursor.fetchall()
        for record in records:
            return record[0]
        
    transform = DbtTaskGroup(
        group_id='transform',
        project_config = cosmos_config.DBT_PROJECT_CONFIG,
        profile_config = cosmos_config.DBT_CONFIG,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/transform']
        )
    )

    chain(
        upload_sql_stat,
        create_imdb_dataset,
        upload_idb_dataset,
        check_load(),
        transform,
        check_transform(),
    )

sentiment_pipeline()



