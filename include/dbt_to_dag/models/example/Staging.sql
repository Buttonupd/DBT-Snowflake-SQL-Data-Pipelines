with source_data as (

    SELECT * FROM RecentMockData
    WHERE Gender='Male'
)

select *
from source_data

