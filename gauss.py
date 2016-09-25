#!/usr/bin/python3.5

import sys
import numpy

print("Input file is", sys.argv[1])
in_file = open(sys.argv[1], 'r')
N = int(in_file.readline())
print("N =", N)
eps = float(in_file.readline())
print("eps =", eps)

b = numpy.empty(N, numpy.float64)
for i in range(0, N):
    b[i] = numpy.float64(in_file.readline())
print("b =\n", b)

A = numpy.empty((N, N) , numpy.float64)
for i in range(0, N):
    for j in range(0, N):
        A[i][j] = numpy.float64(in_file.readline())
print("A =\n", A)

def solve():
    for j in range(0, N):
#        print("j =", j)
        b[j] = b[j]/A[j][j]
        A[j] = A[j]/A[j][j]
        for i in range(0, N):
            if (i != j):
                b[i] -= b[j] * A[i][j]
                A[i] -= A[j] * A[i][j]
                if (count_greater_then_eps(A[i], eps) == 0):
                    if (abs(b[i]) < eps):
                        print("Infinite number of solutions")
                        print("b =\n", b)   
                        print("A =\n", A)
                        return 
                    else:
                        print("System is inconsistent")
                        return
#    print("b =\n", b)   
#    print("A =\n", A)
    print("x=\n", b)

def count_greater_then_eps(x, epsilon):
    cnt = 0
    for x_i in x:
       if (abs(x_i) > epsilon): 
           cnt += 1 
    return cnt

solve()

print("Output file is", sys.argv[2])
out_file = open(sys.argv[2], 'w')
for i in range(0, N):
    out_file.write(str(b[i]) + "\n")
