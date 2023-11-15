def kruskalMST(G):
    # 가중치 기준으로 오름차순 정렬
    sorted_G = sorted(G, key=lambda x: x[2])

    T = []

    # 각 노드의 부모 노드 저장하는 딕셔너리
    parent = {node: node for edge in G for node in edge[:2]}

    while len(T) < len(G) - 1:
        if not sorted_G:
            break

        # 가장 작은 가중치 가져오기
        e = sorted_G.pop(0)
        a, b, weight = e

        # 간선 e가 사이클을 만들지 않을 경우
        if parent[a] != parent[b]:
            T.append(e)

            # 두 노드를 연결하기 위해 한 노드의 부모를 다른 노드로 설정
            parent_a, parent_b = parent[a], parent[b]
            for node in parent:
                if parent[node] == parent_a:
                    parent[node] = parent_b

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
