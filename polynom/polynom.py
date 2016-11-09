#!/usr/bin/python3

import sys
import math

def polynom_val(t, x, c, N):
    val = c[0]
    for i in range(1, N):
        m = 1
        for j in range(0, i):
            m = m * (t - x[j])
        val += m * c[i]
    return val

if (len(sys.argv) != 3):
    print("usage:", sys.argv[0], "<input_file> <output_file>")
    exit(1)

in_file = open(sys.argv[1], 'r')
print("Input file is", sys.argv[1])
out_file = open(sys.argv[2], 'w')
print("Output file is", sys.argv[2])
N = int(in_file.readline())
print("N =", N)

x = []
for i in range(0, N):
    x.append(float(in_file.readline()))
    if (i == 1):
        min_h = abs(x[0] - x[1])
    elif (i > 1):
        h = abs(x[i] - x[i - 1])
        if (h < min_h):
            min_h = h

print("min_h =", min_h)

f_0 = []
for i in range(0, N):
    f_0.append(float(in_file.readline()))
print("f[0] =", f_0)

f = f_0.copy()
c = [f[0]]
for i in range(1, N):
    for j in range(0, N - i):
        f[j] = (f[j + 1] - f[j]) / (x[j + i] - x[j])
    print("f[", i, "] = ", f, sep = '')
    c.append(f[0])

print("c = ", c)

h = min_h / 10
for i in range(0, N):
    t = x[i]
    out_file.write(str(t) + "," + str(polynom_val(t, x, c, N)) + "," + str(f_0[i])+ "\n")
    t += h
    while (i != N - 1) and (t < x[i + 1]):
        out_file.write(str(t) + "," + str(polynom_val(t, x, c, N)) + "\n")
        t += h

