#!/usr/bin/python3

import sys
import numpy

print("Task file is", sys.argv[1])
task_file = open(sys.argv[1], 'r')
print("Input file 1 is", sys.argv[2])
in1_file = open(sys.argv[2], 'r')
print("Input file 2 is", sys.argv[3])
in2_file = open(sys.argv[3], 'r')

N = int(task_file.readline())
print("N =", N)
eps = numpy.float64(task_file.readline())
print("eps =", eps)

ok_cnt = 0
for i in range(0, N):
    x_i = numpy.float64(in1_file.readline()) - numpy.float64(in2_file.readline())
    if x_i <= eps:
        print(x_i, "ok")
        ok_cnt += 1
    else: 
        print(x_i)

if (ok_cnt == N):
    print("Test passed")
else:
    print("Test failed")
