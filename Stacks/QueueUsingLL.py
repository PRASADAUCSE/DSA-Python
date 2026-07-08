class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.curr_size = 0

    def offer(self, element):
        new_node = Node(element)
        if self.rear == None or self.front == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.curr_size += 1
        return "Element added successfully"
    
    def poll(self):
        if self.rear == None or self.front == None:
            return "Queue Underflow"
        else:
            element = self.front
            self.front = element.next
            if self.front == None:
                self.rear = None
            self.curr_size -= 1
        return element.data
        
    def peek(self):
        if self.rear == None or self.front == None:
            return "Queue is empty"
        else:
            return self.front.data
        
    def length(self):
        return self.curr_size
    
    def print(self):
        start = self.front
        if start is None:
            print("Queue is empty")
        else:
            while start is not None:
                print(start.data, end=" ")
                start = start.next

que  = Queue()
print(que.peek())
print(que.poll())
que.offer(23)
que.offer(45)
que.offer(67)   

que.print()  # Output: 23 45 67
print(que.poll())
print(que.peek())  # Output: 45
que.offer(89)

que.print()  # Output: 45 67 89
