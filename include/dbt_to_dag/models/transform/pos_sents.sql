SELECT * FROM
    {{ref('aggregate_imdb')}}

WHERE sentiment = 1
ORDER BY sentiment ASC