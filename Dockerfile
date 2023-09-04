FROM quay.io/astronomer/astro-runtime:9.0.0

RUN python -m venv soda_env &&  source soda_env/bin/activate && \
    pip install --no-cache-dir soda-core-bigquery && \
    pip install --no-cache-dir soda-core-scientific && deactivate
