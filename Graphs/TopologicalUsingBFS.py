from collections import deque

n = 6
Adj = [[], [], [3], [1], [0, 1], [0, 2]]

# 1. Initialize indegree array with zeros
indegree = [0] * n

# 2. Count incoming edges for each node
for neighbours in Adj:
    for node in neighbours:
        indegree[node] += 1

# 3. Add all nodes with 0 indegree to the queue
queue = deque([node for node, count in enumerate(indegree) if count == 0])

result = []

# 4. Process the graph
while queue:
    node = queue.popleft()
    result.append(node)

    for neighbour in Adj[node]:
        indegree[neighbour] -= 1
        if indegree[neighbour] == 0:
            queue.append(neighbour)

print(result)  # Output: [4, 5, 0, 2, 3, 1]