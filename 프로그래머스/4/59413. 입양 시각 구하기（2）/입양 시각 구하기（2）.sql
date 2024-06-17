-- 코드를 입력하세요
SET @HOUR = -1; -- (1) HOUR 변수에 먼저 -1을 할당한 후,
SELECT (@HOUR := @HOUR +1) AS HOUR, -- (3) HOUR 변수에 1씩 더해준다
    (SELECT COUNT(HOUR(DATETIME))
    FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23; -- (2) HOUR 변수가 22가 될 때까지