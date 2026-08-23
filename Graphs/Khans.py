from collections import deque
n = 6
Adj = [[], [], [3], [1], [0, 1], [0, 2]]

# Use range(n) so keys are integers (0 to 5)
indegree = {node: 0 for node in range(n)}
queue = deque()
result = []

# Building indegree array
for part in Adj:
    for i in part:
        indegree[i] += 1

# Adding elements to queue if indegree == 0
for node in range(n):
    if indegree[node] == 0:
        queue.append(node)

# BFS
while queue:
    node = queue.popleft()
    result.append(node)

    for neighbour in Adj[node]:
        indegree[neighbour] -= 1

        if indegree[neighbour] == 0:
            queue.append(neighbour)

print(result)