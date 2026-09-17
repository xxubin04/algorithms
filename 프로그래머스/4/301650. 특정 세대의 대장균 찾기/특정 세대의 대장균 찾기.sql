SELECT C.id
FROM ECOLI_DATA A
JOIN ECOLI_DATA B
    ON A.id = B.parent_id
JOIN ECOLI_DATA C
    ON B.id = C.parent_id
WHERE A.parent_id IS NULL
ORDER BY C.id