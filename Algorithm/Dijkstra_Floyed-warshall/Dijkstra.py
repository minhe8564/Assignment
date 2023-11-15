# Dijkstra algorithm
# all pairs shortest path

import heapq
import pandas as pd
import timeit

graph = {
    '서울': {'천안': 12, '원주': 15},
    '천안': {'논산': 4, '대전': 10},
    '논산': {'광주': 13, '대전': 3},
    '광주': {'부산': 15},
    '대전': {'대구': 10},
    '원주': {'대구': 7, '강릉': 21},
    '대구': {'부산': 9},
    '강릉': {'포항': 25},
    '포항': {'부산': 5},
    '부산': {}
}

nodes = graph
data = {node: [] for node in nodes}
for node in nodes:
    for adj_node in nodes:
        data[node].append(graph[node].get(adj_node, '-'))
graph_df = pd.DataFrame(data, index=nodes)

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances

if __name__ == "__main__":
    print("Input Graph")
    print(graph_df.to_csv(sep='\t', index=True))
    print()

    print("Dijkstra Algorithm Result")
    start_node = '서울'

    execution_time = timeit.timeit(
        stmt="dijkstra(graph, start_node)",
        globals=globals(),
        number=10000
    )

    dijkstra_result = dijkstra(graph, start_node)
    print(dijkstra_result)

    print(f"\nExecution Time: {execution_time} seconds")
