import math

A = [[1, 5, -3],
     [2, -3, 4],
     [-2, 4, 2]]

B = [[3, -3, 4],
     [2, 1, 5],
     [1, -6, 1]]

C = [[-2, 1],
     [4, 3],
     [-1, 5]]

D = [[2, 4],
     [-3, 1]]

E = [[1, 0],
     [0, 1]]


def addition(A, B):
    return [[A[r][c] + B[r][c] for c in range(len(A[0]))] for r in range(len(A))]

def multiplication(A, B):
    results = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for r in range(len(A)):
        for c in range(len(B[0])):
            for k in range(len(B)):
                results[r][c] += A[r][k]*B[k][c]
    return results

def determinant(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def rotation(A, angle):
    rotation_matrix = [[math.cos(angle), -math.sin(angle)],
                       [math.sin(angle), math.cos(angle)]]
    return multiplication(rotation_matrix, A)

for row in addition(A, B):
    print(row)
print()

for row in multiplication(A, C):
    print(row)
print()

print(determinant(D),'\n')

for row in rotation(E, math.pi/2):
    row = list(map(lambda x: round(x, ndigits=2), row))
    print(row)
print()