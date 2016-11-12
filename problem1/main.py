#!/usr/bin/python3

import sys
import numpy 
from gauss import gauss

print("Input file is", sys.argv[1])
in_file = open(sys.argv[1], 'r')
N = int(in_file.readline())
print("N =", N)
eps = numpy.float64(in_file.readline())
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

gauss(A, b, N, eps)

print("b =\n", b)   
print("A =\n", A)

print("Output file is", sys.argv[2])
out_file = open(sys.argv[2], 'w')
for i in range(0, N):
    out_file.write(str(b[i]) + "\n")
