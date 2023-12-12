import random

G = [(0, 1, 3), (0, 3, 2), (0, 4, 4), (1, 2, 1), (1, 3, 4), (1, 5, 2), (2, 5, 1), (3, 4, 5), (3, 5, 7), (4, 5, 9)]
v = 6
e = len(G)
T = []
T2 = []
D = [0] * v
#p = random.randrange(0, v)
p = 2
print(f"p: {p}")
D[p] = 0

for j in G:
    if j[0] == p:
        D[j[1]] = j[2]
    elif j[1] == p:
        D[j[0]] = j[2]

for i in range(0, v):
    if D[i] == 0 and i != p:
        D[i] = 99

print(D)
T.append((p, p, 0))
T2.append(p)
print(T2)

while(len(T) < v):
    min = 99
    index_min = -1
    for i in range(0, v):
        if (min > D[i]) == True and (i not in T2) == True:
            min = D[i]
            index_min = i
        print(f"min: {min}")
        print(f"index_min: = {index_min}")

    for a, b, c in G:
        n = 0
        if a == index_min or b == index_min:
            if (a in T2) == True:
                print("a")
                n = a
                if D[index_min] == c:
                    T.append((n, index_min, D[index_min]))
                    break
            elif (b in T2) == True:
                print("b")
                n = b
                if D[index_min] == c:
                    T.append((n, index_min, D[index_min]))
                    break
            print(f"n: {n}") 
    T2.append(index_min)       

    print(f"T2 = {T2}")
    print(f"T: {T}")

    for j in G:
        if j[0] == index_min and D[j[1]] > j[2]:
            D[j[1]] = j[2]
        elif j[1] == index_min and D[j[0]] > j[2]:
            D[j[0]] = j[2]
    print(f"D: {D}")

print(f"T: {T}")
print(f"T2: {T2}")
T.pop(0)

for i in T:
    print(i)
