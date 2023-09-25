{{ config(materialized = 'table', schema = 'warehouse') }}

WITH
cars_src AS (
    SELECT *
    FROM {{ ref('cars') }}
)

SELECT *
FROM cars_src
WHERE hp > 200
