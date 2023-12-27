from collections import deque

# 이동할 네 방향 정의
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, x, y):
    n = len(graph)
    
    q = deque() # 큐 생성
    q.append((x, y)) # 큐에 현재 좌표 넣기
    
    graph[x][y] = 0  # 다시 방문하지 않도록 현재좌표값을 0으로 바꿔주기
    
    cnt = 1 # 집 개수 카운트(초기화)
    
    while q: # 큐가 빌때까지 반복
        x, y = q.popleft()
        
        for i in range(4): # 현재 위치에서 네 방향으로 위치 확인
            next_x = x + dx[i] # 이동 후의 x좌표(행)
            next_y = y + dy[i] # 이동 후의 y좌표(열)
            
            # 지도를 벗어난 경우 무시
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                continue
                
            # 집이 없는 곳(0)을 만난 경우 무시
            if graph[next_x][next_y] == 0:
                continue
                
            # 해당 위치가 집이 있는 곳(1)인 경우
            if graph[next_x][next_y] == 1:
                graph[next_x][next_y] = 0 # 다시 방문하지 않도록 현재 좌표값을 0으로 바꾸고
                q.append((next_x, next_y)) # 큐에 좌표를 넣고
                cnt += 1 # 집 개수 카운트
                
    return cnt # bfs함수를 호출할 경우 집 개수가 리턴됨
                
# 입력
n = int(input()) # 지도의 크기
graph = [list(map(int, input())) for _ in range(n)] # n*n개의 집 유무 정보 (있으면 1, 없으면 0)

home = [] # 단지별 집 개수를 넣을 빈 리스트 생성
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append(bfs(graph, i, j)) # 리스트에 집 개수 추가
            
home.sort() # 단지별 집 개수 리스트 오름차순 정리

# 정답출력
print(len(home))
for i in range(len(home)):
    print(home[i])