

def dfs(sn, visited, adj):
    visited.add(sn)
    print(sn, end=' ')
    for i in adj[sn]:
        if i not in visited:
            dfs(i, visited, adj)

adj_list = [[1, 2], [0, 3], [0, 3, 4], [1, 2], [2]]

visited = set()

dfs(0, visited, adj_list)