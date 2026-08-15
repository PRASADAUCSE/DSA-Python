n = 8
Adj_list = [[1], [0,2,7], [1,3], [2,4,6], [3,5], [4], [3,7], [1,6]]
colors = [-1]*n

def dfs(sn, colors, Adj_list, depth=0):
    indent = "  " * depth
    print(f"{indent}→ Visiting node {sn} (color: {colors[sn]})")
    
    for neighbours in Adj_list[sn]:
        print(f"{indent}  Checking neighbour {neighbours}")
        
        #if no colour for neighbour
        if(colors[neighbours] == -1):
            colors[neighbours] = 1-colors[sn]
            print(f"{indent}    Unvisited! Assigned color {colors[neighbours]} to node {neighbours}")
            if (dfs(neighbours, colors, Adj_list, depth+1) == False):
                return False
        elif colors[neighbours] == colors[sn]:
            print(f"{indent}    ❌ CONFLICT! Node {neighbours} has same color {colors[neighbours]} as node {sn}")
            return False
        else:
            print(f"{indent}    ✓ OK - Node {neighbours} already has different color {colors[neighbours]}")
    
    print(f"{indent}← Backtrack from node {sn}")
    return True


print("=" * 50)
print("DRY RUN: Bipartite Graph Detection using DFS")
print("=" * 50)
print(f"Adjacency List: {Adj_list}\n")

is_bipartite = True
for i in range(n):
    if(colors[i] == -1):
        print(f"\n[Start DFS from component {i}]")
        colors[i] = 0
        print(f"Assigned color 0 to node {i}")
        if(dfs(i, colors, Adj_list) == False):
            is_bipartite = False
            break

print("\n" + "=" * 50)
print(f"Result: Is Bipartite: {is_bipartite}")
print(f"Final Colors: {colors}")
print("=" * 50)

