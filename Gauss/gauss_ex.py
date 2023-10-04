from numpy import array, zeros, append
import numpy as np

def gausselim(A, b):
    #AUGMENTED MATRIX
    augA = np.c_[A,b]
    p1 = augA [1,:] - augA [0,:] * (augA [1,0] / augA [0,0])
    p2 = augA [2,:] - augA [0,:] * (augA [2,0] / augA [0,0])
    temp = append(augA[0,:], p1)
    augA1 = append(temp, p2).reshape(3,4)
    p3 = augA1[2,:] - augA1[1,:] * (augA1[2,1] / augA1[1,1])
    augA2 = augA1.copy()
    augA2[2] = p3
    A = augA2[:,0:3]
    b = augA2[:,-1]

    #BACKSUBTTUTION
    x = zeros((3))
    x[2] = b[2] / A[2,2]
    x[1] = (b[1] - A[1,2] * x[2]) / A[1,1]
    x[0] = (b[0] - A[0,2] * x[2] - A[0,1] * x[1]) / A[0,0]

    return x

with open('gauss_in.txt', 'r') as f:
    data = f.read()

lines = data.strip().split('\n\n')

A = array([list(map(int, row.split())) for row in lines[0].split('\n')])
b = array(list(map(int, lines[1].split())))
xg = gausselim(A, b)

with open('gauss_out.txt', 'w') as f:
    f.write('x1 = %8.4f, x2 = %8.4f, x3 = %8.4f' % (xg[0], xg[1], xg[2]))