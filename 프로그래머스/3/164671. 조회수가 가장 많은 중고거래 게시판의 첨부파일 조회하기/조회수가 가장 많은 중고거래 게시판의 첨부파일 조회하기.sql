-- 코드를 입력하세요
WITH MAXVIEW AS(
    SELECT BOARD_ID, VIEWS
    FROM USED_GOODS_BOARD
    ORDER BY 2 DESC
    LIMIT 1
)
SELECT CONCAT('/home/grep/src/', m.BOARD_ID, '/', f.FILE_ID, f.FILE_NAME, f.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE f
JOIN MAXVIEW m ON f.BOARD_ID=m.BOARD_ID
ORDER BY f.FILE_ID DESC;