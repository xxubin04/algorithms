# WITH PER_RANK AS(
#     SELECT
#         id,
#         size_of_colony,
#         PERCENT_RANK() OVER(ORDER BY size_of_colony DESC) AS per_rank
#     FROM ECOLI_DATA
# )

WITH PER_RANK AS(
    SELECT
        ID,
        SIZE_OF_COLONY,
        PERCENT_RANK() OVER(
            ORDER BY SIZE_OF_COLONY DESC
        ) AS per_rank
    FROM ECOLI_DATA
)

SELECT ID,
    CASE
        WHEN per_rank <= 0.25 THEN 'CRITICAL'
        WHEN per_rank <= 0.5 THEN 'HIGH'
        WHEN per_rank <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM PER_RANK
ORDER BY ID


# SELECT id,
#     CASE
#         WHEN per_rank <= 0.25 THEN 'CRITICAL'
#         WHEN per_rank <= 0.5 THEN 'HIGH'
#         WHEN per_rank <= 0.75 THEN 'MEDIUM'
#         ELSE 'LOW'
#     END AS colony_name
# FROM PER_RANK
# ORDER BY id'









