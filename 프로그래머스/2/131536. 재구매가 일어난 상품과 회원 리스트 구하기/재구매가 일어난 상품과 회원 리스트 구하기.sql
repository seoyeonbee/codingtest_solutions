-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY 2, 1 -- 상품ID별로 묶었을 때
HAVING COUNT(USER_ID) > 1 -- 해당 상품ID에 대한 회원ID 수가 1보다 클 경우
ORDER BY 1, 2 DESC;