import math

class Graph:
    def __init__(self, graph):
        self.V = len(graph)
        self.edges = graph

    def kruskal(self):
        self.edges.sort(key=lambda x: x[2])
        T = []
        parent = list(range(self.V))

        def find(i):
            if parent[i] == i:
                return i
            return find(parent[i])

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                parent[root_x] = root_y

        while len(T) < self.V - 1:
            if not self.edges:
                break
            u, v, w = self.edges.pop(0)
            if find(u) != find(v):
                T.append((u, v, w))
                union(u, v)

        return T

    def tsp(self, start_node, mst):  # 시작점과 mst를 인자로 받음
        visited = set()              # 방문한 노드 set
        path = []                    # tsp

        def dfs(node):
            visited.add(node)        # 방문 노드 추가 
            path.append(node)        # tsp에 추가

            for edge in mst:            # loop mst
                if node in edge[:2]:    # 현재 노드가 해당 간선에 속한다면
                    neighbor = edge[0] if edge[1] == node else edge[1]  # 이웃 노드 결정
                    if neighbor not in visited:  # 이웃 노드가 방문되지 않았다면
                        dfs(neighbor)            # 재귀적으로 이웃 노드를 탐색

        dfs(start_node)
        path.append(start_node)  # 시작 노드로 돌아오는 것을 보장하기 위해 시작 노드를 경로에 추가

        return path


def cal_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


cities = {'A': (0, 3), 'B': (7, 5), 'C': (6, 0), 'D': (4, 3),
          'E': (1, 0), 'F': (5, 3), 'H': (4, 1), 'G': (2, 2)}

# 노드 간의 거리를 저장할 리스트 초기화
distances = []
city_indices = {city: index for index, city in enumerate(cities)}

# 각 노드 쌍에 대한 거리 계산 및 저장
for city1, coord1 in cities.items():
    for city2, coord2 in cities.items():
        if city1 != city2:
            distance = cal_distance(coord1, coord2)
            index1, index2 = city_indices[city1], city_indices[city2]
            distances.append((index1, index2, distance))

# 그래프 초기화 및 간선 추가
graph = Graph(distances)

# 최소 신장 트리 계산
minimum_spanning_tree = graph.kruskal()

# TSP 경로 계산
start_node = 0
tsp = graph.tsp(start_node, minimum_spanning_tree)

# 경로 출력
city_names = {index: city for city, index in city_indices.items()}
tsp = [city_names[index] for index in tsp]
print("TSP Path:", tsp)

# 총 이동 거리 계산
total_distance = sum(cal_distance(cities[tsp[i]], cities[tsp[i + 1]]) for i in range(len(tsp) - 1))
print("Total Distance:", total_distance)