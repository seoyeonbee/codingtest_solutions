-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK_SALES bs
JOIN BOOK b ON bs.BOOK_ID = b.BOOK_ID
WHERE DATE_FORMAT(bs.SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY 1
ORDER BY 1;