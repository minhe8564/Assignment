# Floyd algorithm
# all pairs shortest path

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

def floyd_warshall(graph):
    nodes = list(graph.keys())
    n = len(nodes)

    distances = {i: {j: float('inf') for j in nodes} for i in nodes}
    for i in nodes:
        distances[i][i] = 0
        for j, weight in graph[i].items():
            distances[i][j] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances

if __name__ == "__main__":
    print("Input Graph")
    print(graph_df.to_csv(sep='\t', index=True))
    print()

    print("Floyd-Warshall Algorithm Result")

    execution_time = timeit.timeit(
        stmt="floyd_warshall(graph)",
        globals=globals(),
        number=10000
    )

    floyd_warshall_result = floyd_warshall(graph)
    print(floyd_warshall_result)

    print(f"\nExecution Time: {execution_time} seconds")
