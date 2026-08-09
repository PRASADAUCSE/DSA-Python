import heapq

arr = []

heapq.heappush(arr, -10)
heapq.heappush(arr, -70)
heapq.heappush(arr, -50)
heapq.heappush(arr, -5)

print([-x for x in arr])  # Print the heap as a list of positive values

print(-heapq.heappop(arr))