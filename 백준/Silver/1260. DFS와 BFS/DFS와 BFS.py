from collections import deque

n, m, v = map(int, input().split()) # 정점 개수, 간선 개수, 시작점 번호
graph = [[False] * (n+1) for _ in range(n+1)] # 각 정점의 연결정보를 표현할 2차원 리스트 생성(False로 초기화)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True # 정점 a와 b가 연결되어있다는 의미

visited_d = [False] * (n+1) # dfs의 방문기록
visited_b = [False] * (n+1) # bfs의 방문기록


def dfs(v):
    visited_d[v] = True # 현재 노드 방문처리
    print(v, end = " ") # 탐색 완료한 v노드 출력
    
    for i in range(1, n+1):
        if not visited_d[i] and graph[v][i]: # i번째 노드가 아직 방문하지 않은 v노드의 인접노드라면
            dfs(i)


def bfs(v):
    queue = deque([v]) # 큐 생성과 동시에 시작점 넣기
    visited_b[v] = True # 방문처리
    
    while queue : 
        v = queue.popleft() # 큐의 첫번째 원소 꺼내서 v에 지정
        print(v, end = " ") # 탐색 완료한 v노드 출력
        
        for i in range(1, n+1):
            if not visited_b[i] and graph[v][i]: # i번째 노드가 아직 방문하지 않은 v노드의 인접노드라면
                queue.append(i) # 큐에 해당 i번째 노드 추가하고
                visited_b[i] = True # 방문처리

# 결과출력
dfs(v)
print()
bfs(v)