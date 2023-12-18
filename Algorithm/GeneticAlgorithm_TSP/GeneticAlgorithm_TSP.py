import math
import random

# 두 도시 사이의 거리 계산
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# 경로의 총 거리 계산
def calculate_total_distance(path, city_coordinates):
    total_distance = 0
    for i in range(len(path) - 1):
        city1 = path[i]
        city2 = path[i + 1]
        total_distance += calculate_distance(city_coordinates[city1], city_coordinates[city2])
    return total_distance

# Cycle Crossover 수행 함수
def cycle_crossover(parent1, parent2):
    size = len(parent1)
    child = [None] * size
    indexes = set(range(size))

    start_index = random.choice(list(indexes))
    current_index = start_index

    while True:
        child[current_index] = parent1[current_index]
        indexes.discard(current_index)
        current_index = parent2.index(parent1[current_index])

        if current_index == start_index:
            break

    for i in indexes:
        child[i] = parent2[i]

    return child

# 돌연변이 수행 함수
def mutate(path, mutation_rate):
    for i in range(len(path)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(path) - 1)
            path[i], path[j] = path[j], path[i]
    return path

# TSP를 위한 유전 알고리즘
def genetic_algorithm(city_coordinates, population_size, generations, crossover_rate, mutation_rate):
    cities = list(city_coordinates.keys())
    population = [random.sample(cities, len(cities)) for _ in range(population_size)]

    for generation in range(generations):
        # 각 개체의 적합도 계산
        fitness_scores = [1 / calculate_total_distance(individual, city_coordinates) for individual in population]

        # 적합도에 기반하여 부모 선택
        parents = random.choices(population, weights=fitness_scores, k=population_size)

        # Cycle Crossover를 사용하여 자손 생성
        offspring = []
        for i in range(0, population_size, 2):
            if random.random() < crossover_rate:
                child1 = cycle_crossover(parents[i], parents[i + 1])
                child2 = cycle_crossover(parents[i + 1], parents[i])
            else:
                child1 = parents[i].copy()
                child2 = parents[i + 1].copy()
            offspring.extend([child1, child2])

        # 자손에 돌연변이 적용
        for i in range(population_size):
            offspring[i] = mutate(offspring[i], mutation_rate)

        # 이전 개체 모집단을 새로운 개체 모집단으로 대체
        population = offspring

    # 최종 모집단에서 가장 좋은 개체 찾기
    best_individual = max(population, key=lambda x: 1 / calculate_total_distance(x, city_coordinates))
    best_distance = calculate_total_distance(best_individual, city_coordinates)

    return best_individual, best_distance

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

# 알고리즘 매개변수 설정
population_size = 8
generations = 100
crossover_rate = 1.0
mutation_rate = 0.01

# 유전 알고리즘 실행
best_path, best_distance = genetic_algorithm(cities, population_size, generations, crossover_rate, mutation_rate)

# 결과 출력
print("최적 이동 순서:", best_path)
print("최적 이동 거리:", best_distance)
