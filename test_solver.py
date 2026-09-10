# test_solver.py
from simplex_solver import simplex

c = [3, 2]           # Objective: Maximize 3x + 2y
A = [[1, 2], [4, 0]] # Constraints: x + 2y <= 8, 4x <= 16
b = [8, 16]

res = simplex(c, A, b)
print(res)