{{ config(materialized='table')}}

WITH source_data AS (
    SELECT TOP 10000 * FROM {{ source('dbo', 'Comm')}}
)

SELECT * FROM source_data