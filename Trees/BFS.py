from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None
        
def bfs(root):
    if root is None:
        return []
    visited = deque([root])
    result = []
    while visited:
        level_size = len(visited)
        level_nodes = []
        for _ in range(level_size):
            current = visited.popleft()
            level_nodes.append(current.data)

            if current.left is not None:
                visited.append(current.left)
            if current.right is not None:
                visited.append(current.right)

        result.append(level_nodes)

    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.left.right = Node(7)

print(bfs(root))
                


