n=5
edges = 6
arr = [(1,3) , (1,2) , (2,3) , (2,4) , (3,5) , (4,5)]

matrix = [[0]*(n+1) for i in range(n+1)]

for u,v in arr:
    matrix[u][v] = 1
    #matrix[v][u] = 1

print("Adjacency Matrix:")
for row in range(1,n+1):
    print(matrix[row][1:])