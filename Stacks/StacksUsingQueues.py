from collections import deque
class Stack:
    def __init__(self):
        self.que = deque()

    def push(self, x):
        if len(self.que) == 0:
            self.que.append(x)
        else:
            self.que.append(x)

        while(self.que[0] != x):
            self.que.append(self.que[0])
            self.que.popleft()
        return "element added succesfully"
    
    def pop(self):
       
        return self.que.popleft()
    
    def top(self):
        if len(self.que) == 0:
            return "noting to peek"
        return self.que[0]
    
    #return self.que.peek()
    
    def length(self):
        return len(self.que)
    

value = Stack()
value.push(21)
value.push(33)
print(value.length())
print(value.top()) #33
print(value.pop())  #33
print(value.top()) #21
print(value.pop())
print(value.pop())
print(value.top())
print(value.length())
        

