from cosmos.config import ProfileConfig,ProjectConfig
from pathlib import Path

DBT_CONFIG = ProfileConfig(
    profile_name='imdb',
    target_name='gcs_dev',
    profiles_yml_filepath='/usr/local/airflow/include/dbt_to_dag/profiles.yml'
)

DBT_PROJECT_CONFIG = ProjectConfig(
    dbt_project_path = '/usr/local/airflow/include/dbt_to_dag/'
)

