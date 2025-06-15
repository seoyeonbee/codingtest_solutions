WITH
    RENT AS( -- 대여 이력과 트럭 정보 조인 (대여 기간을 구하기 위함)
        SELECT
            HISTORY_ID,
            h.CAR_ID,
            CAR_TYPE,
            DAILY_FEE,
            DATEDIFF(END_DATE, START_DATE) + 1 AS DURATION, -- 대여기간
            CASE
                WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 7 AND DATEDIFF(END_DATE, START_DATE) + 1 < 30 THEN '7'
                WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 AND DATEDIFF(END_DATE, START_DATE) + 1 < 90 THEN '30'
                WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 90 THEN '90'
            END AS DURATION_TYPE -- 대여기간 종류
        FROM CAR_RENTAL_COMPANY_CAR c
        LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h ON c.CAR_ID = h.CAR_ID
        WHERE CAR_TYPE = '트럭' -- 트럭 필터링
    )

, TRUCK_RENT_PLAN AS( -- 트럭 대여 정보만 남김
    SELECT 
        PLAN_ID,
        REPLACE(DURATION_TYPE, '일 이상', '') AS DURATION_TYPE, -- '일 이상' 부분 제거
        DISCOUNT_RATE -- ex. 5, 8, 15 ..
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    WHERE CAR_TYPE = '트럭'
)

, RENT_PLAN AS(
    SELECT
        HISTORY_ID,
        CASE
            WHEN r.DURATION_TYPE IS NULL THEN DAILY_FEE * DURATION -- 할인정책이 없는 대여기간일 경우(정가)
            ELSE (DAILY_FEE * (100-DISCOUNT_RATE)/100) * DURATION -- 할인정책 적용된 경우(=일일 요금 * 할인율 * 대여일수)
        END AS FEE
    FROM RENT r
    LEFT JOIN TRUCK_RENT_PLAN t ON r.DURATION_TYPE = t.DURATION_TYPE
)

-- 최종조회
SELECT 
    HISTORY_ID,
    FLOOR(FEE) AS FEE
FROM RENT_PLAN
ORDER BY 2 DESC, 1 DESC;