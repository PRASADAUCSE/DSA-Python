class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.left.right = Node(7)

print(root.data)
print(root.left.data)
print(root.right.data)
