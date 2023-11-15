def primMST(G):
    p = G[0][0] # 임의의 시작점 p 선택
    n = len(set([v for u, v, _ in G])) + 1  # 전체 vertex 수

    # D 배열 초기화
    D = [float('inf')] * n
    D[p] = 0

    # T 초기화
    T = set()
    T.add(p)
    MST = []

    while len(T) < n:
        v_min = None
        min_weight = float('inf')

        # T에 속하지 않은 각 점 v에 대하여 D[v]가 최소인 점 v_min 찾기
        for v, u, weight in G:
            if u in T and v not in T and weight < D[v]:
                D[v] = weight
            if v in T and u not in T and weight < D[u]:
                D[u] = weight

        # T에 추가할 점과 간선 찾기
        for v in range(n):
            if v not in T and D[v] < min_weight:
                v_min = v
                min_weight = D[v]

        # T에 v_min과 연결된 간선 추가
        for u, v, weight in G:
            if ((u == v_min and v in T) or (v == v_min and u in T)) and weight == D[v_min]:
                MST.append((u, v, weight))
                T.add(v_min)

    return MST

# 파일 읽기
G = []
with open('input_prim.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.replace('(', '').replace(')', '')
        parts = line.split(',')
        a, b, c = map(int, parts)
        G.append((a, b, c))

MST = primMST(G)

# 파일 저장
with open('output_prim.txt', 'w') as f:
    for item in MST:
        f.write(f"({item[0]}, {item[1]}, {item[2]})\n")
v
