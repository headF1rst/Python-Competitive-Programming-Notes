import sys
import heapq
input = sys.stdin.readline
INF = int(1e9) # 무한대 값

# 노드, 간선의 개수 입력
v, e = map(int, input().split())
# 시작지점 값 입력
start = int(input())
# 모든 간선에 대한 정보를 담는 배열
G = [[] for i in range(v + 1)]
# 최단거리 테이블을 무한대로 초기화
distance = [INF] * (v + 1)

# 모든 간선의 정보 입력
for _ in range(e):
    s, e, cost = map(int, input().split())
    # 방향 그래프인 경우
    G[s].append((e, cost))
    # 무방향 그래프의 경우 G[e].append(s, c) 추가

# 다익스트라 알고리즘
def dijkstra(start):
    # 미방문 노드 저장하는 우선순위 큐 (최단거리, 탐색노드)
    q = [(0, start)]
    # 시작노드 초기화
    distance[start] = 0

    # 큐가 빌때까지 반복. BFS수행
    while q:
        # 미방문 노드중 거리가 가장 작은 노드 삭제
        dist, curNode = heapq.heappop(q)
        # 이미 처리된 노드이면 패스
        if distance[curNode] < dist: continue
        # BFS 수행노드의 인접노드의 최단경로값을 확인
        for i in G[curNode]:
            cost = dist + i[1]
            # 현재 노드에서 인접노드로 가는 경로값이 더 작은 경우 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 시작노드로 부터 각 노드까지의 최단경로를 출력
for i in range(1, v + 1):
    if distance[i] == INF: print("INFINITY")
    else: print(distance[i])