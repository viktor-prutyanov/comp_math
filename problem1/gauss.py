#!/usr/bin/python3

import numpy

def swap_rows(arr, src, dst):
    if (src != dst):
        arr[[src, dst],:] = arr[[dst, src],:]

def backward_pass(A, b, N, eps):
    for i in range(0, N):
        zeros_cnt = 0
        for j in range(0, N):
            if abs(A[i][j]) <= eps:
                zeros_cnt += 1
        if (zeros_cnt == N):
            if abs(b[i]) <= eps: 
                print("Too many solutions")
            else: 
                print("No solutions")
            return False
    for i in reversed(range(0, N)):
        for k in reversed(range(0, i)):
            b[k] -= b[i] * A[k][i]
            A[k] -= A[i] * A[k][i]

def forward_pass(A, b, N, eps):
    for i in range(0, N):
        if abs(A[i][i]) <= eps:
            for k in range(i + 1, N):
                if abs(A[k][i]) <= eps:
                    if (k == N - 1):
                        print("Too many solutions")
                        return False
                else:
                    swap_rows(A, i, k)
                    break
        if abs(A[i][i]) > eps:
            b[i] = b[i]/A[i][i]
            A[i] = A[i]/A[i][i]
        for k in range(i + 1, N):
            b[k] -= b[i] * A[k][i]
            A[k] -= A[i] * A[k][i]
    return True

def gauss(A, b, N, eps):
    if forward_pass(A, b, N, eps):
        return backward_pass(A, b, N, eps)
    else:
        return False
