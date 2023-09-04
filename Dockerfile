FROM quay.io/astronomer/astro-runtime:9.0.0

RUN source dbt-env/bin activate && \
    pip install --no-cache-dir soda-core-bigquery && \
    pip install --no-cache-dir soda-core-scientific && deactivate
