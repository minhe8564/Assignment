import numpy as np
import random
from itertools import permutations, combinations
from tqdm import tqdm

# 가중치 그래프 클래스
class WeightedGraph:
    def __init__(self):
        self.V = set()
        self.E = []

    def add_vertex(self, vertex):
        self.V.add(vertex)

    def add_edge(self, u, v, weight):
        self.E.append((u, v, weight))
        self.E.append((v, u, weight))
        self.add_vertex(u)
        self.add_vertex(v)

    def get_weight(self, u, v):
        for edge in self.E:
            if (edge[0] == u and edge[1] == v) or (edge[0] == v and edge[1] == u):
                return edge[2]
        return None


# 적합도 평가 함수
def calculate_fitness(individual, graph):
    total_distance = 0
    path = individual.copy()
    path.append(individual[0])
    for i in range(len(path) - 1):
        start_vertex, end_vertex = path[i], path[i+1]
        weight = graph.get_weight(start_vertex, end_vertex)
        if weight:
            total_distance += weight
    return total_distance


# 사이클 교차 연산 함수
def cycle_crossover(parent1, parent2):
    size = len(parent1)
    child = [None] * size
    visited = [False] * size

    cycle_start = random.randint(0, size - 1)
    current = cycle_start

    while True:
        child[current] = parent1[current]
        visited[current] = True
        next_index = parent2.index(parent1[current])

        if visited[next_index]:
            break

        current = next_index

    for i in range(size):
        if child[i] is None:
            child[i] = parent2[i]

    return child


# 돌연 변이 연산 함수
def mutate(individual):
    if random.random() < mutation_ratio:
        #print('기습 변이')
        mutation_point1, mutation_point2 = random.sample(range(len(individual)), 2)
        individual[mutation_point1], individual[mutation_point2] = individual[mutation_point2], individual[mutation_point1]
    return individual


# 정점
points = {'A': (0, 3), 'B': (7, 5), 'C': (6, 0), 'D': (4, 3),
          'E': (1, 0), 'F': (5, 3), 'H': (4, 1), 'G': (2, 2)}
# 정점 간 거리 계산
comb = list(combinations(points, 2))
data = [(i, j, np.linalg.norm(np.array(points[i]) - np.array(points[j]))) for i, j in comb]
# 가중치 그래프 초기화
graph = WeightedGraph()
for edge in data:
    graph.add_edge(edge[0], edge[1], edge[2])


# 유전 알고리즘 파라미터
population_size = 8
crossover_ratio = 1.0
mutation_ratio = 0.01
max_generations = 1000


# 초기 개체 생성
population = [list(perm) for perm in permutations(points.keys())][:population_size]
# 초기화된 best_fitness 값을 무한대로 설정
best_fitness = float('inf')

# 메인 유전 알고리즘
for generation in tqdm(range(max_generations)):

    # 개체 평가
    fitness_scores = [calculate_fitness(individual, graph) for individual in population]

    # 최적 개체 선택
    best_index = fitness_scores.index(min(fitness_scores))
    best_individual = population[best_index]
    best_fitness = fitness_scores[best_index]

    # 새로운 세대 생성
    new_population = [best_individual]

    while len(new_population) < population_size:
        # 부모 선택
        parent1 = random.choice(population)
        parent2 = random.choice(population)

        # 교차 연산
        if random.random() < crossover_ratio:
            child = cycle_crossover(parent1, parent2)
        else:
            child = parent1

        # 돌연변이 연산
        child = mutate(child)

        # 새로운 개체 추가
        new_population.append(child)

    # 세대 교체
    population = new_population
best_individual.append(best_individual[0])

#결과 출력
print('-'.join(best_individual),'|',best_fitness)
