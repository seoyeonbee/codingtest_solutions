n = int(input()) # 카드 개수
level = sorted(list(map(int, input().split())), reverse = True) # 카드별 레벨(내림차순 정렬)

max_card = level[0] # 가장 레벨이 큰 카드 저장
gold = sum(level[:2]) # 골드 저장(가장 레벨이 큰 카드 + 그다음으로 큰 카드 로 초기화)

for i in range(2, n): # 인덱스 2부터 순회
    gold += (max_card + level[i]) # 가장 레벨이 큰 카드 + 나머지 카드의 레벨을 차례로 누적
    
print(gold) # 정답 출력