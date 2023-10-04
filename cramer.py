from numpy import array, zeros
from numpy.linalg import det

def cramer(A,b):
    n = len(b)
    detsub = zeros((n))
    x = zeros((n))
    detA = det(A)
    for i in range(n):
        Atemp = A.copy()
        Atemp[:,i] = b
        detsub[i] = det(Atemp)
        x[i] = detsub[i]/detA
    return detsub, x

with open('cramer_in.txt', 'r') as f:
    data = f.read()

lines = data.strip().split('\n\n')

A = array([list(map(int, row.split())) for row in lines[0].split('\n')])
b = array(list(map(int, lines[1].split())))

detsub, x = cramer(A,b)

with open('cramer_out.txt', 'w') as f:
    with open('cramer_out.txt', 'w') as f:
        f.write('x1 = %.17f, x2 = %.17f, x3 = %.17f' % (x[0], x[1], x[2]))
