''' 모든 노드에서 모든 노드로 가는 최단거리 구하는 플로이드 와샬 알고리즘 '''
INF = int(1e9)

# 노드의 개수 v, 간선의 개수 e 입력받기
v, e = map(int, input().split())
# 모든 노드에서 모든 노드로 가는 최단 거리 저장을 위한 2차원 배열 생성
# 초기값은 무한대로 초기화
G = [[INF] * (v + 1) for _ in range(v + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if a == b:
            G[a][b] = 0

# 각 간선에 대한 정보 입력
for _ in range(e):
    # a에서 b로 가는 비용 c
    a, b, c = map(int, input().split())
    G[a][b] = min(G[a][b], c)
    
# 점화식에 따라 플로이드 워셜 알고리즘 수행 
for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            G[a][b] = min(G[a][b], G[a][k] + G[k][b])
            
# 모든 노드에서 모든 노드로 가는 최단 경로 출력
for a in range(1, v + 1):
    for b in range(1, v + 1):
        # 도달할 수 없는 경우, INFINITY 출력
        if G[a][b] == INF: print("INFINITY", end=" ")
        # 도달할 수 있는 경우, 거리를 출력
        else: print(G[a][b], end=" ")
    print()