from collections import deque
n=6
Adj = [[], [], [3], [1], [0,1], [0,2]]
indegree = {node:0 for node in range(n)}
queue = deque()
result= []

#building indegree array
for part in Adj:
    for i in part:
        indegree[i] +=1

#adding elements to queue if indegeee == 0
for part in Adj:
    if indegree[part] == 0:
        queue.append(part)


#BFS
while (queue != None):
    node = queue.popleft()
    result.append(node)

    for neighbour in Adj[node]:
        indegree[neighbour]-=1

        if indegree[neighbour]==0:
            queue.append(neighbour)


print(result)


