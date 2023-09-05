--Override dbt_project file materialize attribute

with source_data as (

    SELECT review, sentiment 
    FROM {{source('imdb', 'raw_imdb')}}
    GROUP BY sentiment, review
    ORDER BY sentiment ASC
)

select *
from source_data