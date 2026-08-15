from collections import deque

sn = 0
n=10
# Mapping: a=0, b=1, c=2, d=3, e=4, f=5, g=6, h=7, i=8, j=9
adj_list = [[1],[0,2],[1,3,9],[2,4],[3,5],[4,6,8],[5,7],[6],[5,9],[2,8]]
queue = deque() 
colors = [-1]*n


queue.append(sn)
colors[sn] = 0

while queue:
    node = queue.popleft()

    for neighbours in adj_list[node]:
        if (colors[neighbours] == -1):
            colors[neighbours] = 1-colors[node]
            queue.append(neighbours)

        elif colors[neighbours] == colors[node]:
            print(False)
            break
print(True)

        
