from collections import deque

''' BFS 시작'''
def BFS(G, start, visited):
    q = deque([start])
    # 현재 시작 노드를 방문처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 하나의 원소를 뽑아 출력
        curNode = q.popleft()
        print(curNode, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for nextNode in G[curNode]:
            if not visited[nextNode]:
                q.append(nextNode)
                visited[nextNode] = True

# 각 노드의 방문 여부를 표현
visited = [False] * 9

# 각 노드가 연결된 정보를 리스트 자료형으로 표현
G = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

BFS(G, 1, visited)