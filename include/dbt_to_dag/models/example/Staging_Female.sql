-- Create a view that references Staging table


select *

from {{ ref('Staging') }}

WHERE Gender='Female'

