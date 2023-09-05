--Override dbt_project file materialize attribute

with source_data as (

    SELECT  * FROM {{source('imdb', 'raw_imdb')}}
)

select *
from source_data