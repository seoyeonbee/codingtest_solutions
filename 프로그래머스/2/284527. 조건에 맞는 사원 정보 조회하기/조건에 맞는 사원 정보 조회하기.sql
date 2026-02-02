WITH ranks AS(
    SELECT
        g.SCORE,
        g.EMP_NO,
        e.EMP_NAME,
        e.POSITION,
        e.EMAIL,
        ROW_NUMBER() OVER(ORDER BY g.SCORE DESC) AS RNK
    FROM(
        SELECT
            EMP_NO,
            SUM(SCORE) AS SCORE
        FROM HR_GRADE
        GROUP BY 1
    ) AS g
    JOIN HR_EMPLOYEES e ON G.EMP_NO = e.EMP_NO
)

SELECT
    SCORE,
    EMP_NO,
    EMP_NAME,
    POSITION,
    EMAIL
FROM ranks
WHERE RNK = 1