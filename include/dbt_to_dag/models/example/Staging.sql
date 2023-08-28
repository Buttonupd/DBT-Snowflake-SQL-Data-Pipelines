--Override dbt_project file materialize attribute

with source_data as (

    SELECT * FROM RecentMockData
)

select *
from source_data

