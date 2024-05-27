# Legacy Multiplication
""" import numpy as numpy
import random
import time

def mm(matrix1, matrix2):
    result = []

    for i, row in enumerate(matrix1):
        newRow = []
        for j, col in enumerate(row):
            dot_product = sum(matrix1[i][i] * matrix2[k][j] for k in range(len(matrix2)))
            newRow.append(dot_product)
        result.append(newRow)

    return result

def create_matrix(n):
    return [[random.random() for i in range(n)] for i in range(n)]

start_time = time.monotonic()

N = 1024

a = create_matrix(N)
b = create_matrix(N)

C = mm(a,b)

# print(C)

end_time = time.monotonic()

print(end_time - start_time) """

# Cuda way


from numba import cuda 
import numpy as np
import math
import time

@cuda.jit
def matmul_kernel(A,B,C):
    sA = cuda.shared.array(shape=(TPB, TPB), dtype=np.float32)
    sB = cuda.shared.array(shape=(TPB, TPB), dtype=np.float32)

    x,y = cuda.grid(2)

# Keine Lust alles zu schreiben, video weiter schauen








