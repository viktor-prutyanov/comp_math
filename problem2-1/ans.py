#!/usr/bin/python3

import sys
import math

def a(x):
    return -3.29983 + 2/math.pow((1+x),1.5) + (2*x)/math.pow((1+x), 1.5) + 0.666667*math.sqrt(1+x) + 0.666667*x*math.sqrt(1+x)

out_file = open("ans.csv", 'w')
out_file.write("x, y\n")

x = 0.0
N = 1000
for i in range(0, N):
    x += 1.0/N
    out_file.write(str(x) + "," + str(a(x)) + "\n")