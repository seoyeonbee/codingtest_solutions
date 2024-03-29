-- 코드를 입력하세요
SELECT info.REST_ID,
    info.REST_NAME,
    info.FOOD_TYPE,
    info.FAVORITES,
    info.ADDRESS,
    ROUND(AVG(re.REVIEW_SCORE), 2) AS SCORE -- 리뷰 평균점수 소수점세번째 자리에서 반올림
FROM REST_INFO info
INNER JOIN REST_REVIEW re
ON info.REST_ID = re.REST_ID
WHERE info.ADDRESS LIKE '서울%' -- 서울에 위치한 식당에 한해서
GROUP BY info.REST_NAME -- 각 식당별로
ORDER BY SCORE DESC, FAVORITES DESC;