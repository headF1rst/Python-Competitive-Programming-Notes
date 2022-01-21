# 정점, 간선 입력받기
v, e = map(int, input().split())
# 부모 테이블 조기화
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i
    
# 사이클 발생 여부 초기화
cycle = False

''' union-find '''

# x노드의 부모 노드를 찾아서 반환
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

''' 사이클 형성 여부 판단 '''
for i in range(e):
    # 서로 연결된 두 정점 a, b
    a, b = map(int, input().split())
    
    # 정점 a, b가 같은 부모를 갖고있으므로 사이클 형성
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았으면 합집합(union) 수행
    else:
        union_parent(parent, a, b)