def kruskalMST(G):
    # 부모 노드 찾기
    def find(node):
        if parent[node] == node:
            return node
        return find(parent[node])

    # 두 집합 합치기
    def union(v, e):
        root1 = find(v)
        root2 = find(e)
        parent[root1] = root2

    # 가중치 기준으로 오름차순 정렬
    sorted_G = sorted(G, key=lambda x: x[2])
    T = []
    parent = {}

    # MST
    for edge in sorted_G:
        a, b, weight = edge
        if a not in parent:
            parent[a] = a
        if b not in parent:
            parent[b] = b

        if find(a) != find(b):
            T.append(edge)
            union(a, b)

    return T

G = []

# 파일 읽기
with open('input_kruskal.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()

        line = line.replace('(', '').replace(')', '')
        parts = line.split(',')

        a, b, c = map(int, parts)
        G.append((a, b, c))

MST = kruskalMST(G)

# 파일 저장
with open('output_kruskal.txt', 'w') as f:
    for item in MST:
        f.write(f"({item[0]}, {item[1]}, {item[2]})\n")
