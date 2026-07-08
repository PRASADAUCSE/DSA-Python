class Stack:
    def __init__(self):
        self.items = [0] * 5
        self.top = -1

    def push(self, item):
        if self.top >= 4:
            print("Stack Overflow")
        else:
            self.top += 1
            self.items[self.top] = item

    def pop(self):
        if self.top <=-1:
            return "Stack Underflow"
            
        else:
            self.top -= 1
            return self.items[self.top + 1]
        
    def peek(self):
        if self.top <= -1:
            return "Nothing to peek"
        else:
            return self.items[self.top]
        
    def length(self):
        return self.top + 1
    
st  = Stack()

print(st.pop())

