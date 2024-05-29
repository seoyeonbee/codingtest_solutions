-- 코드를 작성해주세요
WITH FE AS(
    SELECT SUM(CODE)
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
)
SELECT
    CASE
        WHEN SKILL_CODE & (SELECT * FROM FE) AND SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME='Python') THEN 'A'
        WHEN SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME='C#') THEN 'B'
        WHEN SKILL_CODE & (SELECT * FROM FE) THEN 'C'
        ELSE NULL
    END AS GRADE, ID, EMAIL

FROM DEVELOPERS
HAVING GRADE IS NOT NULL
ORDER BY 1, 2;