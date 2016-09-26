#!/usr/bin/python3

import sys
import numpy

N = int(sys.argv[1])
eps = numpy.float64(sys.argv[2])
A = numpy.random.rand(N, N) * 10
x = numpy.random.rand(N, 1) * 10
b = A.dot(x)

print("Task file is", sys.argv[3])
out_file = open(sys.argv[3], 'w')
print("Answer file is", sys.argv[4])
ans_file = open(sys.argv[4], 'w')

out_file.write(str(N) + "\n")
out_file.write(str(eps) + "\n")
for i in range(0, N):
    out_file.write(str(b[i][0]) + "\n")
print("b = \n", b)
for i in range(0, N):
    for j in range(0, N):
        out_file.write(str(A[i][j]) + "\n")
print("A = \n", A)

for i in range(0, N):
    ans_file.write(str(x[i][0]) + "\n")
print("x = \n", x)
