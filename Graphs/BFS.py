from collections import deque

def bfs(sn, adj_list):
    visited = set()
    queue = deque([sn])
    visited.add(sn)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i  in adj_list[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

adj_list = [[1, 2], [0, 3], [0, 3, 4], [1, 2], [2]]
bfs(0, adj_list)