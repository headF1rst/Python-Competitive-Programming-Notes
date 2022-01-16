''' DFS 시작 '''
def DFS(G, v, visted):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for nextNode in G[v]:
        if not visited[nextNode]:
            DFS(G, nextNode, visited)

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

DFS(G, 1, visited)