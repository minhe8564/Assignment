import numpy as np

# 점 정보
points = {'A': (0, 3), 'B': (7, 5), 'C': (6, 0), 'D': (4, 3),
          'E': (1, 0), 'F': (5, 3), 'H': (4, 1), 'G': (2, 2)}

# 함수: 두 지점 간의 거리 계산
def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# 함수: 후보해의 이동 거리 계산
def calculate_total_distance(solution):
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += calculate_distance(points[solution[i]], points[solution[i + 1]])
    return total_distance

# 함수: 돌연변이 연산
def mutate(solution):
    mutated_solution = solution.copy()
    idx1, idx2 = np.random.choice(len(solution), 2, replace=False)
    mutated_solution[idx1], mutated_solution[idx2] = mutated_solution[idx2], mutated_solution[idx1]
    return mutated_solution



# 함수: 사이클 교차 연산
def cycle_crossover(parent1, parent2):
    # 사이클 교차 연산을 위한 초기 설정
    cycle = []
    start_idx = np.random.randint(0, len(parent1))
    current_city = parent1[start_idx]

    # 교차 연산 진행
    while True:
        cycle.append(current_city)
        idx_in_parent2 = parent2.index(current_city)
        current_city = parent1[idx_in_parent2]

        if current_city == parent1[start_idx]:
            break

    # 교차된 부분을 추출하여 자식 후보해 생성
    child = [-1] * len(parent1)
    for city in cycle:
        child[parent1.index(city)] = city

    # 나머지 부분은 부모 2의 해당 위치의 도시로 채움
    for i in range(len(child)):
        if child[i] == -1:
            child[i] = parent2[i]

    return child


# 함수: Genetic Algorithm 구현
def genetic_algorithm(num_candidates, crossover_ratio, mutation_ratio, max_generations):
    
    # 초기 후보해 생성
    initial_population = [list(points.keys()) for _ in range(num_candidates)]
    for i in range(num_candidates):
        np.random.shuffle(initial_population[i])
        

    for generation in range(max_generations):
        # 평가
        fitness_scores = [1 / calculate_total_distance(candidate) for candidate in initial_population]

        # 룰렛 휠 선택
        selected_indices = np.random.choice(np.arange(num_candidates), num_candidates, p=fitness_scores / np.sum(fitness_scores))
        selected_population = [initial_population[i] for i in selected_indices]
        

        # 교차 연산
        new_population = []
        for i in range(0, num_candidates, 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i + 1]

            # 교차 연산 수행
            if np.random.rand() < crossover_ratio:
                child1 = cycle_crossover(parent1, parent2)
                child2 = cycle_crossover(parent2, parent1)
            else:
                child1, child2 = parent1.copy(), parent2.copy()

            new_population.extend([child1, child2])


        # 돌연변이 연산
        for i in range(num_candidates):
            if np.random.rand() < mutation_ratio:
                new_population[i] = mutate(new_population[i])

        initial_population = new_population

    # 최종 후보해 선택
    final_fitness_scores = [1 / calculate_total_distance(candidate) for candidate in initial_population]
    best_index = np.argmax(final_fitness_scores)
    best_solution = initial_population[best_index]
    best_solution.append(best_solution[0])

    return best_solution, calculate_total_distance(best_solution)

# 알고리즘 실행
best_solution, best_distance = genetic_algorithm(num_candidates=8, crossover_ratio=1.0, mutation_ratio=0.01, max_generations=5)

# 결과 출력
print("이동 순서:", best_solution)
print("이동 거리:", best_distance)
