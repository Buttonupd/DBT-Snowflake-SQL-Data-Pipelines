SELECT * FROM 
    {{ref('aggregate_imdb')}}
WHERE sentiment = 0
ORDER BY sentiment ASC