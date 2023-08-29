--Override dbt_project file materialize attribute

with source_data as (

    SELECT business_logic FROM schema_name
)

select *
from source_data

