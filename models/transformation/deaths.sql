{{ config(materialized = 'table', schema = 'warehouse') }}

WITH
src AS (
    SELECT *
    FROM {{source('dbt_airflow', 'covid_csv')}}
)

SELECT death
FROM src