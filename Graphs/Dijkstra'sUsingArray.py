source = 1
Adj_list = [[],[(2,3), (4,5)], [], [(2,-10)], [(3,2)]]

n = len(Adj_list) - 1
distance_arr = [float('inf')]*(n+1)
visited_arr = [False]*(n+1)

distance_arr[source] = 0

#searching for perfect neighbour
for i in range(1,n+1):
    neighbour = -1
    for node in range(1,n+1):
        if (visited_arr[node] != True) and (neighbour==-1 or distance_arr[node]<distance_arr[neighbour]):
            neighbour = node

    visited_arr[neighbour] = True
    #Relaxation
    for v, weight in Adj_list[neighbour]:
        if(distance_arr[neighbour] + weight <distance_arr[v]):
            distance_arr[v] = distance_arr[neighbour] + weight

print(distance_arr)

