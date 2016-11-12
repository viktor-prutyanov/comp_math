#!/usr/bin/python3

import sys
import random
import math

out_file = open(sys.argv[1], 'w') 
N = int(sys.argv[2])
out_file.write(str(N) + "\n")

X = sorted([random.random() for i in range(0, N)])
F = [math.sin(10 * x) for x in X]

for a in X + F:
    out_file.write(str(a) + "\n")
