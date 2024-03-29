-- 코드를 입력하세요
SELECT * -- 전체 조회
FROM( -- 서브쿼리 생성(전체 정렬을 위해서)
    SELECT DATE_FORMAT(ons.SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
        ons.PRODUCT_ID,
        ons.USER_ID AS USER_ID,
        ons.SALES_AMOUNT
    FROM ONLINE_SALE ons
    WHERE DATE_FORMAT(ons.SALES_DATE, '%Y-%m') = '2022-03'

    UNION

    SELECT DATE_FORMAT(ofs.SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
        ofs.PRODUCT_ID,
        NULL AS USER_ID, -- 없는 컬럼은 NULL로 채우기
        ofs.SALES_AMOUNT
    FROM OFFLINE_SALE ofs
    WHERE DATE_FORMAT(ofs.SALES_DATE, '%Y-%m') = '2022-03'
) AS result
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID; -- 병합한 데이터 전체 정렬

