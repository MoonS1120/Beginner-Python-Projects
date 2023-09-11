A = [[1, 5, -3],
     [2, -3, 4],
     [-2, 4, 2]]

B = [[3, -3, 4],
     [2, 1, 5],
     [1, -6, 1]]

C = [[-2, 1],
     [4, 3],
     [-1, 5]]

def addition(A, B):
    return [[A[r][c] + B[r][c] for c in range(len(A[r]))] for r in range(len(A))]

def multiplication(A, B):
    results = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for r in range(len(A)):
        for c in range(len(B[0])):
            for k in range(len(B)):
                results[r][c] += A[r][k]*B[k][c]
    return results

for row in addition(A, B):
    print(row)
print()

for row in multiplication(A, C):
    print(row)
print()