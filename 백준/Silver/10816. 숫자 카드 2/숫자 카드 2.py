n = int(input()) # 갖고 있는 숫자 카드 개수 N
card = sorted(list(map(int, input().split()))) # 갖고 있는 숫자 카드 리스트(이진탐색을 위해 오름차순 정렬)
m = int(input()) # 탐색해야 할 숫자 카드 개수 M
target = list(map(int, input().split())) # 탐색해야 할 숫자 카드 리스트

cnt = {} # 탐색한 숫자 카드 카운팅 리스트 (0으로 초기화)

# 탐색해야 할 카드 별 카운팅 횟수 누적
for i in card:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

# 정답 출력
for i in target:
    if i in cnt:
        print(cnt[i], end = ' ')
    else:
        print(0, end = ' ')