import sys
t = int(input()) # 테스트케이스 수

for _ in range(t): # 각 테스트케이스 별 반복문 수행
    n, m = map(int, input().split()) # 문서 수, 탐색할 문서 인덱스
    doc = list(enumerate(list(map(int, sys.stdin.readline().split())))) # 문서 별 중요도를 담은 리스트
    v = doc[m] # (탐색할 문서 중요도, 인덱스)가 묶인 값을 튜플형태로 저장
    prnt = 0 # 탐색할 문서의 프린트 순서(0으로 초기화)
    
    while doc: # doc이 빌 때까지 반복
        max_v = max([i[1] for i in doc]) # doc에서 가장 높은 중요도 저장
        
        if doc[0][1] == max_v: # 현재 doc의 첫번째 문서 중요도가 max_v일 경우
            front = doc.pop(0) # 현재 doc의 첫번째 문서 중요도를 front에 저장
            prnt += 1 # 프린트 순서 증가
            if front == v:
                print(prnt) # 정답 출력하고
                break # 반복문 탈출
                
        else: # 현재 doc의 첫번째 문서 중요도가 max_v가 아닐 경우
            front = doc.pop(0) # 해당 원소를 뽑아서 front에 담아두고
            doc.append(front) # doc의 맨 뒤로 보낸다.