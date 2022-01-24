from collections import deque

# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
# 모든 노드의 진입차수 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
G = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력
for _ in range(e):
    a, b = map(int, input().split())
    G[a].append(b) # 정점 a에서 b로 가는 간선
    indegree[b] += 1 # b노드로 들어오는 진입차수 1 증가

''' 위상정렬 시작 '''
def topology_sort():
    result = [] # 알고리즘 수행 결과를 저장
    q = deque()

    # 진입 차수가 0인 노드를 큐에 삽입하고 시작
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.pop() # 큐에서 다음 노드 꺼내기
        result.append(now)
        # 해당 노드와 연결된 노드들의 진입차수에서 1 빼기
        for i in G[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬 수행 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()