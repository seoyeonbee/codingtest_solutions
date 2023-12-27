# 이동할 네 방향 정의
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    # 지도를 벗어난 경우 즉시 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if graph[x][y] == 1: # 현재 노드가 집이 있는 곳이라면
        global cnt # (함수 밖에서도 사용할 수 있도록) 집 개수 카운팅을 위한 전역 변수 설정
        cnt += 1 # 집 개수 카운팅
        
        graph[x][y] = 0 # 다시 방문하지 않도록 현재좌표값을 0으로 바꿔주기
        
        for i in range(4): # 현재 위치에서 네 방향으로 위치 확인
            next_x = x + dx[i] # 이동 후의 x좌표(행)
            next_y = y + dy[i] # 이동 후의 y좌표(열)
            dfs(next_x, next_y) # 이동 후 위치에서 재귀적으로 dfs 호출
        return True
    
    return False # 그 외(집이 없는 곳) 종료

                
# 입력
n = int(input()) # 지도의 크기
graph = [list(map(int, input())) for _ in range(n)] # n*n개의 집 유무 정보 (있으면 1, 없으면 0)

cnt = 0 # 집 개수
home = [] # 단지별 집 개수를 넣을 빈 리스트 생성
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            home.append(cnt) # 리스트에 집 개수 추가
            cnt = 0 # 집 개수 초기화 (다른 단지를 돌아야 하므로)
            
home.sort() # 단지별 집 개수 리스트 오름차순 정리

# 정답출력
print(len(home))
for i in range(len(home)):
    print(home[i])