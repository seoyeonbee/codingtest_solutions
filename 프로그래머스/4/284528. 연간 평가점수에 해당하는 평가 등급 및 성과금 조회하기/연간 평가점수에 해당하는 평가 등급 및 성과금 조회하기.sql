-- 코드를 작성해주세요
WITH EMP_GRADE AS (
    SELECT e.EMP_NO, e.EMP_NAME, e.DEPT_ID, e.SAL,
        CASE
            WHEN AVG(g.SCORE) >= 96 THEN 'S'
            WHEN (AVG(g.SCORE) >= 90 AND AVG(g.SCORE) < 96) THEN 'A'
            WHEN (AVG(g.SCORE) >= 80 AND AVG(g.SCORE) < 90) THEN 'B'
            WHEN AVG(g.SCORE) < 80 THEN 'C'
            ELSE NULL
        END AS GRADE
    FROM HR_EMPLOYEES e
    JOIN HR_GRADE g ON e.EMP_NO=g.EMP_NO
    -- WHERE g.HALF_YEAR = 2 -- 정확하게 어떤 반기의 등급인지(ex. 상반기와 하반기의 평균인지) 모르겠음..
    GROUP BY 1
)
SELECT EMP_NO, EMP_NAME, GRADE,
    CASE
        WHEN GRADE = 'S' THEN SAL * 0.2
        WHEN GRADE = 'A' THEN SAL * 0.15
        WHEN GRADE = 'B' THEN SAL * 0.1
        WHEN GRADE = 'C' THEN SAL * 0
        ELSE NULL
    END AS BONUS
FROM EMP_GRADE
ORDER BY 1;