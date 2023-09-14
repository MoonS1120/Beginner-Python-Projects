import numpy as np
A = np.array([[1, 5, -3], [2, -3, 4], [-2, 4, 2]])

B = np.array([[3, -3, 4], [2, 1, 5], [1, -6, 1]])

C = np.array([[-2, 1], [4, 3], [-1, 5]])

D = np.array([[2, 4], [-3, 1]])

E = np.array([[1, 0], [0, 1]])

print(A+B)
print(A.dot(C))
print(f"{np.linalg.det(D):.2f}")