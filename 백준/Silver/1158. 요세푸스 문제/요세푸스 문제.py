from collections import deque

n, k = map(int, input().split())
people = [i for i in range(1, n+1)] # 주어진 사람들 번호를 넣은 리스트 생성
people = deque(people) # 데크(큐)로 변환

answer = [] # 제거된 사람들을 넣을 리스트 생성

while people: # 주어진 사람들이 모두 제거될 때까지 반복
    people.rotate(-(k-1)) # 먼저 k-1칸 만큼 왼쪽으로 회전
    answer.append(str(people.popleft())) # 정답용 리스트에 회전시킨 상태에서 맨 앞 원소 추출후 추가
    
print("<", ", ".join(answer)[:], ">", sep="") # 정답 출력