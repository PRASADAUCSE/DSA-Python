Adj_list = [[(1,2), (2,4)],
            [(2,7), (3,5), (4,6)],
            [(0,4), (1,7)],
            [(1,5), (4,1)],
            [(1,6), (3,1)]
            ]

edges = []
n = len(Adj_list)
visited_arr = [0]*n

for i in range(n):
    for neighbour, wt in Adj_list[i]:
        if(i<neighbour):
            edges.append((wt, neighbour, i))


edges.sort(key = lambda x:x[0])
print(edges)

mst = []
min_cost = 0


def dfs(edges, visited_arr):

    for wt, i, node in edges:
        if(visited_arr[i] == 0):
            if(dfs(edges, visited_arr) == True):
                return True
        
        elif(visited_arr[i] == 1 and i != parent):
            return True

    return False

for wt, node, parent in edges:
    #checking for cycle detection
    if(dfs(edges, visited_arr) == False):
        mst.append((parent, node))
        min_cost += wt


print(mst)
print(min_cost)