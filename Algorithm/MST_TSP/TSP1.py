import math

rf = open("input.txt","r")
vertex = int(rf.readline()) # 파일로부터 점의 개수를 입력받습니다.

def dot2dot(a,b):
    x = a[0]-b[0]
    y = a[1]-b[1]
    return math.sqrt(x**2+y**2)
## 피타고라스의 정리를 이용해 점과 점 사이의 거리를 구하는 함수입니다.

MST = [] # MST를 저장하는 리스트입니다.
TSP = [] # TSP를 해결하기 위해 이동경로를 저장하는 리스트입니다.
TravelPath = 0 # 이동거리를 저장합니다.
startdot = 0 # MST와 TSP를 위한 임의의 시작점입니다.(처음에는 0으로 설정)
xy = [[0]*2 for i in range(vertex)] # 각 점의 x,y 좌표 정보입니다.
valueFrom = [startdot for i in range(vertex)] # 트리에서 갈 수 있는 최소값을 찾았을 때, MST에 적어주기 위해 어떤 점에서 출발하는지 알기 위한 리스트입니다.
visited = [False for i in range(vertex)] # 트리에 포함된 점으로는 연결되지 않게 하기 위해, 방문 정보를 저장하는 리스트입니다. 

dist = [[0 for i in range(vertex)] for i in range(vertex)]
for i in range(vertex):
    xy[i][0],xy[i][1] = map(int,rf.readline().split())
for i in range(vertex):
    for j in range(vertex):
        if i!=j:
            dist[i][j] = dot2dot(xy[i],xy[j])
## 각 점의 x,y 좌표를 파일에서 입력받고, 이에 따라 각 점들끼리의 거리를 구합니다.

visited[startdot] = True # 최초 시작하는 점에 대해 방문 정보를 갱신시켜줍니다. 
link = dist[startdot] # 트리의 연결 정보가 저장되는 리스트를 만듭니다.(처음에는 점의 연결 정보 = 트리의 연결 정보)

while len(MST)<vertex:
    n = min(link) 
    nextdot = link.index(n)
    ## 제일 작은 가중치 값을 찾고, 그 가중치 값을 가진 점을 찾습니다. 
    
    strdot = valueFrom[nextdot]
    MST.append([strdot,nextdot])
    ## MST에 찾은 점을 연결합니다.
    
    visited[nextdot] = True # 찾은 점을 연결했기 때문에, 방문으로 표시합니다.
    link[nextdot] = float("Inf") # 후에 link에서 최소값을 찾을 때 혼동을 주지 않게 연결한 점의 가중치를 무한대로 바꿔줍니다.
    
    for i in range(vertex):
        if dist[nextdot][i]<link[i] and not visited[i]: 
            link[i] = dist[nextdot][i]
            valueFrom[i] = nextdot
    ## 만일 찾은 점에 연결된 점 중 현재 연결 정보보다 가중치가 작은 값이 있다면, 갱신해줍니다.
    
MST = MST[1:] 
reverse_MST = [[i[1],i[0]]for i in MST]
MST+=reverse_MST
## 구한 MST와 진행방향을 반대로 하여 두 정보를 합칩니다.

connect = [[] for i in range(vertex)]
for i in MST:
    connect[i[0]].append(i[1])
## TSP를 해결하는 과정에서, 더 수월하게 방향을 찾기위해
## MST 기준 각 노드에서 이동 가능한 노드를 저장하는 리스트를 만듭니다.

now = startdot # 현재의 노드를 의미합니다.
TSP_visited = [0]*vertex # 각 노드에 몇 번 방문했는지에 대한 정보를 저장하는 리스트입니다.

TSP_visited[now]+=1
TSP.append(now)
## 순회를 하기 이전에, 최초 시작하는 점에 대한 정보를 갱신해 줍니다.

Travel = 1 # 노드 간의 이동이 일어날 때마다 1씩 커지는 변수입니다.
previous = vertex+1 # 직전에 방문한 노드를 의미합니다.(처음에는 그림 상에 존재하지 않는 값)


while Travel<=len(MST): # MST + reverse_MST와 길이가 같다 = 순회를 마쳤다
    min_visited = [(TSP_visited[i],i) for i in connect[now] if i!= previous] 
    ## 직전의 노드를 제외하고, 현재 노드에서 이동 가능한 노드들을 각각의 방문 횟수와 함께 가져옵니다.
    
    if len(min_visited):
        min_visited = min(min_visited) # 이동 가능한 노드 중 가장 방문 횟수가 적은 노드를 가져옵니다.
    else:
        min_visited = (TSP_visited[previous],previous) # 이동 가능한 노드가 없다면 직전의 노드로 돌아갑니다.
         
    TSP.append(min_visited[1])
    previous = now
    now = min_visited[1]
    TSP_visited[now]+=1
    Travel+=1
    ## 찾아낸 노드를 기록하고, 필요한 정보들을 갱신해줍니다.
    
result = []
for p in TSP:
    if p not in result:
        result.append(p)
result.append(startdot) # 순회한 기록에서 중복되는 값을 제거합니다.

for i in range(1,len(result)):
    TravelPath += dot2dot(xy[result[i-1]],xy[result[i]]) # 중복값이 제거된 이후, 점과 점 사이의 거리를 구합니다.

result = [chr(r+65) for r in result] # 각 노드를 알파벳으로 변환합니다.
print("이동 순서: "+str(result))
print("이동 거리: "+str(TravelPath))