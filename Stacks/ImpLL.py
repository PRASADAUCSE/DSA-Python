class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            return "Stack Underflow"
        else:
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item
        
    def peek(self):
        if self.top is None:
            return "Nothing to peek"
        else:
            return self.top.data
    
    def length(self):
        count = 0
        current = self.top
        while current is not None:
            count += 1
            current = current.next
        return count
    

st = Stack()

print(st.peek())  # Output: 30
print(st.pop())   # Output: 30
print(st.length()) # Output: 2

