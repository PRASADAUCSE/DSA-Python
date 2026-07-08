class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.curr_size = 0

    def offer(self, element):
        if (self.curr_size == self.size):
            return "Queue Overflow"
        if(self.front == -1 and self.rear == -1):
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element
        self.curr_size += 1
        return "Element added successfully"
    
    def poll(self):
        if(self.curr_size == 0):
            return "Queue Underflow"
        element = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.curr_size -= 1
        return element

    def peek(self):
        if(self.curr_size == 0):
            return "Queue is empty"
        return self.queue[self.front]
    
    def length(self):
        return self.curr_size
    
    def print(self):
        if self.curr_size == 0:
            print("Queue is empty")
        else:
            index = self.front
            for i in range(self.curr_size):
                print(self.queue[index], end=" ")
                index = (index + 1) % self.size
            print()
    
que = Queue(5)

que.offer(23)
que.offer(45)
que.offer(67)



que.print()  # Output: 23 45