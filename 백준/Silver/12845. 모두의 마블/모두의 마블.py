n = int(input()) # 카드 개수
level = sorted(list(map(int, input().split())), reverse = True) # 카드별 레벨(내림차순 정렬)

gold = 0 # 골드 저장(0으로 초기화)

for i in range(1, n): # 레벨이 가장 큰 카드의 다음 인덱스부터 순회
    gold += (level[0] + level[i]) # 가장 레벨이 큰 카드 + 나머지 카드의 레벨을 차례로 누적
    
print(gold) # 정답 출력