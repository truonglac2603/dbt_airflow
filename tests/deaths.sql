{{ config(materialized = 'test', schema = 'warehouse') }}

WITH
src AS (
    SELECT *
    FROM {{source('dbt_airflow', 'covid_csv')}}
)

SELECT *
FROM src
WHERE death >1000000