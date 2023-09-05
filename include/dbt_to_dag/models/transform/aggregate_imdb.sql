--Override dbt_project file materialize attribute

with source_data as (

    SELECT TOP 30000 * FROM raw_imdb
)

select *
from source_data