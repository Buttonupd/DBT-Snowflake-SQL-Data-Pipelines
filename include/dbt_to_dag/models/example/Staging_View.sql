-- Create a view that references Staging table
{{ config(materialize='view') }}

select *
from {{ ref('Staging') }}

