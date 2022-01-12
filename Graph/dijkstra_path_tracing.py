# 출발정점 start 부터 도착정점 end까지의 최소비용을 갖는 경로를 방문하는 정점을 순서대로 출력```

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
# 정점의 수 n
n = int(input())
# 간선의 수 m
m = int(input())

distance = [INF] * (n + 1)
G = [[] for _ in range(n + 1)]
# 역추적 경로를 저장하기 위한 배열. 시작 정점을 -1로 하기위한 초기화
trace = [-1] * (n + 1)
result = []
q = []

for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))

# 출발 정점, 도착 정점
start, end = map(int, input().split())

q.append((0, start))
distance[start] = 0

while q:
    dist, curNode = heapq.heappop(q)
    if distance[curNode] < dist: continue
    for i in G[curNode]:
        nextNode, c = i
        cost = c + dist
        if cost < distance[nextNode]:
            distance[nextNode] = cost
            # 역추적을 위해 trace 배열에 경로를 역으로 기록
            trace[nextNode] = curNode
            heapq.heappush(q, (cost, nextNode))

# start에서 end까지 가는데 드는 최소 비용 출력
print(distance[end])


''' Tracing '''
# 역추적 trace배열에 도착 지점 end를 추가
result.append(end)
while trace[end] != -1:
    result.append(trace[end])
    end = trace[end]

print(len(result))
for i in result[::-1]:
    print(i, end=' ')