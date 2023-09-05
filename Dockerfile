FROM quay.io/astronomer/astro-runtime:9.0.0

RUN python -m venv soda_env &&  source soda_env/bin/activate && \
    pip install --no-cache-dir soda-core-bigquery

RUN python -m venv dbt_env &&  source dbt_env/bin/activate && \
    pip install --no-cache-dir dbt-bigquery && deactivate
    