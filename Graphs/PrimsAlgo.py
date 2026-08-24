import heapq
#from heapq import heapify
source = 0
Adj_list = [[(1,2), (3,6)], 
            [(0,2), (2,3), (4,5), (3,8)], 
            [(4,7), (1,3)], 
            [(0,6), (1,8)], 
            [(1,5), (2,7)]]

n = len(Adj_list)
visited_arr = [False]*n
min_heap= [(0, source, -1)]
heapq.heapify(min_heap)

mst = []
min_cost = 0

while min_heap:
    weight, node, parent = heapq.heappop(min_heap)
    if(visited_arr[node] == False):
        visited_arr[node] = True

        if parent != -1:
            mst.append((parent, node))

        min_cost += weight

        for neighbours, weight in Adj_list[node]:

            if(visited_arr[neighbours] == False):
                heapq.heappush(min_heap, (weight, neighbours, node))


print(mst)
print(min_cost)
