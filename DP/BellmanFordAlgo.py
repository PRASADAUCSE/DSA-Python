source = 0
n = 4
edges = [(0,1,4), (0,3,5), (3,2,3), (2,1,-10),(1,3,-5)]

distance_arr = [float('inf')]*n
distance_arr[source] = 0

def relaxation (edges, distance_arr):
    for u,v, weight  in edges:
        if(distance_arr[u]+weight < distance_arr[v]):
            distance_arr[v] = distance_arr[u]+weight
    return distance_arr

    

for i in range(n-1):
    before = relaxation(edges, distance_arr)

before = distance_arr.copy()


relaxation(edges, distance_arr)
after = distance_arr.copy()
    

print(before == after)
#False -> negative cycle is detected
#True -> no negative cycle

if(before == after):
    print("no negative cycle")

else:
    print("No ans for this question")