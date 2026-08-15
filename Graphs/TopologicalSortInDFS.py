sn = 0
n=6
Adj = [[], [], [3], [1], [0,1], [0,2]]
visited = [0]*n 
st = []

def dfs(sn, visited, Adj, st):
    visited[sn] = 1

    for i in Adj[sn]:
        if(visited[i] == 0):
            dfs(i, visited, Adj, st)

    st.append(sn)


for i in range(n):
    if(visited[i] == 0):
        dfs(i, visited, Adj, st)

print(st[::-1])

