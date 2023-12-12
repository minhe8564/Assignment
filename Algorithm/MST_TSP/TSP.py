import math

# 두 도시 사이의 거리 계산
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Minimum Spanning Tree
# Kruskal Algorithm 사용
def find_mst(edges):
    edges.sort(key=lambda x: x[2])  # 간선을 오름차순으로 정렬
    parent = {}
    rank = {}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    mst = []

    for edge in edges:
        node1, node2, weight = edge
        if node1 not in parent:
            parent[node1] = node1
            rank[node1] = 0
        if node2 not in parent:
            parent[node2] = node2
            rank[node2] = 0

        if find(node1) != find(node2):
            union(node1, node2)
            mst.append(edge)

    return mst

# Traveling Salesman Problem
# BFS Algorithm 사용
def find_tsp_path(mst, start):
    adjacency_list = {}
    for edge in mst:
        city1, city2, _ = edge
        if city1 not in adjacency_list:
            adjacency_list[city1] = []
        if city2 not in adjacency_list:
            adjacency_list[city2] = []

        adjacency_list[city1].append(city2)
        adjacency_list[city2].append(city1)

    visited = set()
    queue = [(start, [start])]
    tsp_path = []

    while queue:
        city, path = queue.pop(0)
        visited.add(city)
        tsp_path.append(city)

        if len(visited) == len(adjacency_list):
            break

        neighbors = adjacency_list[city]
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    tsp_path.append(start)
    return tsp_path

# 중복되는 도시 제거
def remove_duplicates(path):
    unique_path = []
    visited = set()
    for city in path:
        if city not in visited:
            unique_path.append(city)
            visited.add(city)
    return unique_path

def tsp(city_coordinates):
    cities = list(city_coordinates.keys())
    edges = []
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            city1 = cities[i]
            city2 = cities[j]
            distance = calculate_distance(city_coordinates[city1], city_coordinates[city2])
            edges.append((city1, city2, distance))

    mst = find_mst(edges)
    tsp_path = find_tsp_path(mst, 'A')
    unique_path = remove_duplicates(tsp_path)

    total_distance = 0
    for i in range(len(unique_path) - 1):
        city1 = unique_path[i]
        city2 = unique_path[i+1]
        total_distance += calculate_distance(city_coordinates[city1], city_coordinates[city2])

    return unique_path, total_distance

# 각 도시 coordinaies
cities = {
    'A': (0, 3),
    'B': (7, 5),
    'C': (6, 0),
    'D': (4, 3),
    'E': (1, 0),
    'F': (5, 3),
    'H': (4, 1),
    'G': (2, 2)
}

path, distance = tsp(cities)
print("이동 순서:", path)
print("이동 거리:", distance)
