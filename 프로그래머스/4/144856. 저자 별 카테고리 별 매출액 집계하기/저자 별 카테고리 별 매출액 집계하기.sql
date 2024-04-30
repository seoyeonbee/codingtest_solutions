-- 코드를 입력하세요
WITH SB AS(
    SELECT b.BOOK_ID,
            b.CATEGORY,
            b.AUTHOR_ID,
            b.PRICE,
            b.PUBLISHED_DATE,
            bs.SALES_DATE,
            bs.SALES
    FROM BOOK_SALES bs
    JOIN BOOK b ON bs.BOOK_ID=b.BOOK_ID
    WHERE DATE_FORMAT(bs.SALES_DATE, '%Y-%m') = '2022-01'
),
SBA AS(
    SELECT SB.BOOK_ID,
            SB.CATEGORY,
            SB.AUTHOR_ID,
            SB.PRICE,
            SB.PUBLISHED_DATE,
            SB.SALES_DATE,
            SB.SALES,
            a.AUTHOR_NAME
    FROM SB
    JOIN AUTHOR a ON SB.AUTHOR_ID=a.AUTHOR_ID
)
SELECT AUTHOR_ID,
    AUTHOR_NAME,
    CATEGORY,
    SUM(SALES * PRICE) AS TOTAL_SALES
FROM SBA
GROUP BY 1, 3
ORDER BY 1, 3 DESC;