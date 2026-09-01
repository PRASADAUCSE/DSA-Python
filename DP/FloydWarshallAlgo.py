inf = float('inf')
matrix = [
    [0, 3, inf, 7],
    [8, 0, 2, inf],
    [5, inf, 0, 1],
    [2, inf, inf, 0]
]

n = len(matrix)

for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(matrix[i][j], (matrix[i][k] + matrix[k][j]))


print(matrix)