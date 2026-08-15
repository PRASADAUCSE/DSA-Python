n = 7
start = 0
adj_list = [[1, 2], [0, 3], [0, 3, 4], [1, 2], [2], [6], [5]]

visited_arr = [0]*n

def dfs(node, parent, adj_list, visited_arr):


    visited_arr[node] = 1

    for i in adj_list[node]:
        if(visited_arr[i] == 0):
            if(dfs(i, node, adj_list, visited_arr) == True):
                return True
        
        elif(visited_arr[i] == 1 and i != parent):
            return True

    visited_arr[node] = 0
    return False

print(dfs(start, -1, adj_list, visited_arr))
        