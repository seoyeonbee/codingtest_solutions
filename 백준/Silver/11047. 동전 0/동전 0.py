n, k = map(int, input().split()) # 동전 종류, 목표가치
coin = sorted(list(int(input()) for _ in range(n)), reverse = True) # 종류별 동전 가치(내림차순 정렬)
cnt = 0 # 필요한 동전 개수(0으로 초기화)

while k != 0: # k가 0이될때까지 반복
    for i in range(n):
        if coin[i] > k: # 현재 동전의 가치가 목표가치보다 큰 경우
            continue # 종료(for문 처음으로 돌아간다)
        else: # 현재 동전의 가치가 목표가치보다 작은 경우
            cnt += (k//coin[i]) # 필요한 동전 개수: 목표가치를 현재 동전의 가치로 나눈 몫을 누적
            k %= coin[i] # 목표가치: 목표가치를 현재 동전의 가치로 나눈 나머지를 저장
            
print(cnt) # 정답 출력