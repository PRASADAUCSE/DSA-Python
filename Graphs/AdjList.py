n=5
edges = 4
arr = [(0,1) , (0,2) , (2,3) , (2,4)]

adj_list = [[] for i in range(n)]

for u,v in arr:
    adj_list[u].append(v)

for i in range(n):
    print(adj_list[i])